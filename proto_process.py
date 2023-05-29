
import queue
import threading
import datetime

gui_blackbox_data_queue = queue.Queue(300)

blackbox_data_len_dict = \
{
    "time":4,
    "event":2,
    "hd_info":4,
    "bat_vol":2,
    "pack_vol":2,
    "cell_1_vol":2,
    "cell_2_vol":2,
    "cell_3_vol":2,
    "cell_4_vol":2,
    "cell_5_vol":2,
    "cell_6_vol":2,
    "cell_7_vol":2,
    "cell_8_vol":2,
    "cell_9_vol":2,
    "cell_10_vol":2,
    "cell_11_vol":2,
    "cell_12_vol":2,
    "cell_13_vol":2,
    "cell_14_vol":2,
    "cell_15_vol":2,
    "cell_16_vol":2,
    "current":2,
    "cell_temp1":2,
    "cell_temp2":2,
    "board_temp":2,
    "fet_temp":2,
    "soc":1,
    "soh":1,
    "cycle":2,
    "rem_cap":4,
}

class protol_recv_thread(threading.Thread):
    def __init__(self, cur_self, main_self):
        super(protol_recv_thread, self).__init__()
        self.cur_self = cur_self
        self.main_self = main_self
        self.thread = threading.Event()

        self.protol_phase = 0
        self.protol_code = 0
        self.protol_return = 0
        self.protol_len = 0
        self.protol_crc = 0
        self.protol_lock = 0
    def stop(self):
        self.thread.set()
    def stopped(self):
        return self.thread.is_set()

    def check_crc(self):
        sum = 0
        sum += self.protol_return
        sum += self.protol_len
        for item in self.data_list:
            sum += item
        sum = ~sum
        sum += 1
        result = sum
        if sum < 0:
            result = int.from_bytes((sum).to_bytes(4, 'little', signed=True),'little',signed=False)
            result = result & 0x0000ffff
        print("\n check_crc is {}" .format(result))
        return result

    def data_to_int(self, data):
        list = data.split()
        data_int_list = []
        for item in list:
            data_int_list.append(int(item, base=16))
        print("data_to_int data_int_list is {}" .format(data_int_list))
        return data_int_list

    def protol_parse_data(self,data,offset,length):
        if (offset + length) <= len(data):
            if 1 == length:
                return data[offset]
            elif 2 == length:
                return ((data[offset] * (2 ** 8)) + data[offset + 1])
            elif 4 == length:
                return ((data[offset] * (2 ** 24)) + (data[offset + 1] * (2 ** 16)) \
                 + (data[offset + 2] * (2 ** 8)) + data[offset + 3])
            else:
                print("protol_parse_data length error")

    def protol_handle_fun(self,code,data):
        start_offset = 0
        data_item_len = 0
        data_parse_list = []
        if 0x50 == code:
            for item in blackbox_data_len_dict:
                data_item_len = blackbox_data_len_dict[item]
                data_parse_list.append(self.protol_parse_data(data,start_offset,data_item_len))
                start_offset += data_item_len
            gui_blackbox_data_queue.put(data_parse_list)

    def unpack(self,data):
        print("unpack data is {}" .format(data))
        data_int_list = self.data_to_int(data)
        for item in data_int_list:
            if 0 == self.protol_phase:
                if 221 == item:
                    self.protol_code = 0
                    self.protol_return = 0
                    self.protol_len = 0
                    self.protol_crc = 0
                    self.protol_phase = 1
            elif 1 == self.protol_phase:
                self.protol_code = item
                self.protol_phase = 2
            elif 2 == self.protol_phase:
                self.protol_return = item
                if 128 == self.protol_return:
                    self.protol_code = 0
                    self.protol_return = 0
                    self.protol_len = 0
                    self.protol_crc = 0
                    self.protol_phase = 0
                    break
                else:
                    self.protol_phase = 3
            elif 3 == self.protol_phase:
                self.protol_len = item
                self.protol_phase = 4
                self.data_list = []
            elif 4 == self.protol_phase:
                self.data_list.append(item)
                print("len(self.data_list) is {}" .format(len(self.data_list)))
                if self.protol_len == len(self.data_list):
                    self.protol_phase = 5
                    self.crc_list = []
            elif 5 == self.protol_phase:
                self.crc_list.append(item)
                if 2 == len(self.crc_list):
                    self.protol_crc = (self.crc_list[0] * (2 ** 8)) + self.crc_list[1]
                    print("self.protol_crc is {}" .format(self.protol_crc))
                    if self.protol_crc == self.check_crc():
                        self.protol_phase = 6
                    else:
                        self.protol_code = 0
                        self.protol_return = 0
                        self.protol_len = 0
                        self.protol_crc = 0
                        self.protol_phase = 0
                        del self.data_list
                        del self.crc_list
            elif 6 == self.protol_phase:
                if 119 == item:
                    print("process ok")
                    self.protol_handle_fun(self.protol_code,self.data_list)
                self.protol_code = 0
                self.protol_return = 0
                self.protol_len = 0
                self.protol_crc = 0
                self.protol_phase = 0
                del self.data_list
                del self.crc_list
        self.protol_lock = 0

    def run(self):
        while True:
            if self.stopped():
                break
            try:
                if False == self.cur_self.recv_queue.empty() and 0 == self.protol_lock:
                    self.protol_lock = 1
                    data = self.cur_self.recv_queue.get()
                    self.unpack(data)
                else:
                    continue
            except queue.Empty:
                continue
class protol_send_thread(threading.Thread):
    def __init__(self, cur_self, main_self):
        super(protol_send_thread, self).__init__()
        self.cur_self = cur_self
        self.main_self = main_self
        self.thread = threading.Event()

    def stop(self):
        self.thread.set()
    def stopped(self):
        return self.thread.is_set()

    def run(self):
        while True:
            if self.stopped():
                break
            try:
                if False == self.cur_self.send_queue.empty():
                    send_data = self.cur_self.send_queue.get()
                    # data_num = len(send_data)
                    self.cur_self.serial.write(send_data)
                else:
                    continue
            except queue.Empty:
                continue

class protol(object):
    def __init__(self, parent):
        self.parent = parent
        self.recv_queue = queue.Queue(1000)
        self.send_queue = queue.Queue(1000)

    def protol_init(self):
        self.recv_thread = protol_recv_thread(self, self.parent)
        self.send_thread = protol_send_thread(self, self.parent)

    def open_protol_thread(self):
        self.recv_thread.start()
        self.send_thread.start()

    def close_protol_thread(self):
        self.recv_thread.stop()
        self.send_thread.stop()

    def protol_send_func(self, data):
        print("protol_send_func data is {}" .format(data))
        self.send_queue.put(data)

    def protol_recv_func(self, data):
        self.recv_queue.put(data)

    def get_crc(self, data):
        print("get_crc data is {}" .format(data))
        crc_list = []
        sum = 0
        for item in data:
            sum += int(item)
        sum = ~sum
        sum += 1
        result = sum
        if sum < 0:
            result = int.from_bytes((sum).to_bytes(4, 'little', signed=True),'little',signed=False)
            result = result & 0x0000ffff
        print("get_crc result is {}" .format(result))
        crc_list.append(hex(result)[2:4].upper())
        crc_list.append(hex(result)[4:6].upper())
        return crc_list

    # data:[command, len, effective-data],str
    def protol_pack_data(self, data):
        print("protol_pack_data")
        data_len = len(data)
        send_str = 'DD A5'
        send_str = send_str + " " + data[0] # command
        send_str = send_str + " " + data[1]  # len
        if data_len > 1:
            for item in data[2:]:
                send_str = send_str + " " + item
        # get crc
        crc = 0
        crc = self.get_crc(data)
        for item in crc:
            send_str = send_str + " " + item

        send_str = send_str + " " + '77'
        self.protol_send_func(send_str)
        # return send_str


