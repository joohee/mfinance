from packages.cp_code_mgr.codes import CpCodeMgrCode

if __name__ == "__main__":
    header_keys = CpCodeMgrCode.header_dic.keys()
    stock_code_keys = CpCodeMgrCode.stock_code_dic.keys()
    stock_kospi_200_kind_keys = CpCodeMgrCode.stock_kospi_200_kind_dic.keys()
    stock_control_kind_keys = CpCodeMgrCode.stock_control_kind_dic.keys()
    stock_status_kind_dic_keys = CpCodeMgrCode.stock_status_kind_dic.keys()
    stock_supervision_kind_dic_keys = CpCodeMgrCode.stock_supervision_kind_dic.keys()

    for key in sorted(header_keys):
        print("header_dic key: {0}, value: {1}".format(key, CpCodeMgrCode.header_dic.get(key)))
    print("=========================")

