
import queue
import threading
import datetime
import sys

gui_blackbox_data_queue = queue.Queue(300)
bat_basic_data_info_queue = queue.Queue(300)

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

bat_basic_data_len_dict = \
{
    "bat_vol":2,
    "cc":2,
    "rem_capacity":2,
    "moni_capacity":2,
    "cycle":2,
    "fac_data":2,
    "cell_status":4,
    "protec_data":2,
    "sf_ver":1,
    "rsoc":1,
    "fet_status":1,
    "bat_serial_num":1,
    "ntc_num":1,
    "ntc_value_0":2,
    "ntc_value_1":2,
    "ntc_value_2":2,
    "ntc_value_3":2,
}

# bat_basic_info_dict = \
# {
#     "bat_vol":0,
#     "cc":0,
#     "rem_capacity":0,
#     "moni_capacity":0,
#     "cycle":0,
#     "fac_data":0,
#     "cell_status":0,
#     "protec_data":0,
#     "sf_ver":0,
#     "rsoc":0,
#     "fet_status":0,
#     "bat_serial_num":0,
#     "ntc_num":0,
#     "ntc_value_0":0,
#     "ntc_value_1":0,
#     "ntc_value_2":0,
#     "ntc_value_3":0,
# }

class protol_recv_thread(threading.Thread):
    def __init__(self, cur_self, main_self):
        super(protol_recv_thread, self).__init__()
        self.cur_self = cur_self
        self.main_self = main_self
        self.thread = threading.Event()
        
        self.protol_lock = 0
        
    def stop(self):
#         self.thread.set()
        self.thread.clear()
    
    def resume(self):
        self.thread.set()
        
    def stopped(self):
        return self.thread.is_set()
    
    def run(self):
        while True:
            self.thread.wait()
#             if self.stopped():
#                 break
            try:
                if False == self.cur_self.recv_queue.empty() and 0 == self.protol_lock:
                    self.protol_lock = 1
                    data = self.cur_self.recv_queue.get()
                    self.unpack(data)
                    self.protol_lock = 0
                else:
                    self.stop()
#                     continue
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
                    # self.main_self.uart.write(send_data) send_queue
                    self.main_self.uart.uart_send_func(send_data)
                else:
                    continue
            except queue.Empty:
                continue

class protol(object):
    def __init__(self, parent, verbosity=20):
        self.parent = parent
        self.recv_queue = queue.Queue(1000)
        self.send_queue = queue.Queue(1000)
        self.verbosity = verbosity
        self.protol_code = 0
        self.protol_return = 0
        self.protol_len = 0
        self.protol_crc = 0
        self.protol_phase = 0

    def protol_init(self):
        self.recv_thread = protol_recv_thread(self, self.parent)
        self.send_thread = protol_send_thread(self, self.parent)
        
    def debug(self, level, msg):
        if self.verbosity >= level:
            print(msg, file=sys.stderr)

    def open_protol_thread(self):
        self.recv_thread.start()
        self.send_thread.start()

    def close_protol_thread(self):
        self.recv_thread.stop()
        self.send_thread.stop()

    def protol_send_func(self, data):
        print("protol_send_func is {}" .format(data))
        self.send_queue.put(data)
        self.clear_unpack_var()
        self.send_thread.resume()

    def protol_recv_func(self, data):
        self.recv_queue.put(data)
        self.recv_thread.resume()

    def get_crc(self, data):
        sum = 0
        crc_list = []
        for item in data:
            sum += item
        sum = ~sum
        sum += 1
        result = sum
        if sum < 0:
            result = int.from_bytes((sum).to_bytes(4, 'little', signed=True),'little',signed=False)
            result = result & 0x0000ffff
        print("get_crc result is {}" .format(result))
        crc_list.append(int(hex(result)[0:4], 16))
        crc_list.append(int(hex(result)[4:6], 16))
        return crc_list
    
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
        elif 0x03 == code:
            print("recv 0x03 comm data")
            for item in bat_basic_data_len_dict:
                data_item_len = bat_basic_data_len_dict[item]
                data_parse_list.append(self.protol_parse_data(data,start_offset,data_item_len))
                start_offset += data_item_len
            bat_basic_data_info_queue.put(data_parse_list)
            
    def clear_unpack_var(self):
        self.protol_code = 0
        self.protol_return = 0
        self.protol_len = 0
        self.protol_crc = 0
        self.protol_phase = 0

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

    # data:[command, len, effective-data],str
    def protol_pack_data(self, data):
        self.debug(10, "protol_pack_data " + ''.join(str(item) for item in data))
        cmd = data[0]
        data_len = data[1]
        send_str = [0xDD]
        if self.SET_FET_CTRL == cmd:
            send_str.append(0x5A)
        else:
            send_str.append(0xA5)
        send_str.append(cmd)
        send_str.append(data_len)
        if data_len > 0:
            for item in data:
                send_str.append(item)
        # get crc
        crc_list = []
        crc_list = self.get_crc(send_str)
        for item in crc_list:
            send_str.append(item)
        send_str.append(0x77)
        # print("send_str {}".format(send_str))
        self.protol_send_func(send_str)

    def command(self, cmd, description, data):
        self.debug(10, "*** Command: %s" % description)
        send_list = []
        data_len = len(data)
        send_list.append(cmd)
        send_list.append(data_len)
        if data_len > 0:
            for item in data:
                send_list.append(item)
        self.protol_pack_data(send_list)

    def get_board_info(self):
        self.command(self.GET_BOARD_INFO, "get_board_info", [])

    def get_cells_vol(self):
        self.command(self.GET_CELLS_VOL, "get_cells_vol", [])

    def get_basic_data(self):
        self.command(self.GET_BASIC_DATA, "get_basic_data", [])

