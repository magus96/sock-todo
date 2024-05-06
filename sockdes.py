class SocketDeserializer:

    def deserialize(self, req_data: bytes):
        req_data_str = req_data.decode('utf-8')
        req_data_lines = req_data_str.splitlines()
        print(req_data_lines)
        return req_data