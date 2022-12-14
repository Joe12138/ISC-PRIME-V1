class RegulatoryElement:
    def __init__(self, reg_id: int, reg_type: str, subtype: str):
        self.id = reg_id
        self.type = reg_type
        self.subtype = subtype


class SpeedLimit(RegulatoryElement):
    def __init__(self, reg_id: int, reg_type: str, subtype: str, sign_type: str):
        super().__init__(reg_id=reg_id, reg_type=reg_type, subtype=subtype)
        self.sign_type = sign_type
        self.speed_limit_num = self.get_speed_limit_num()

    def get_speed_limit_num(self):
        """
        Get the speed limit number, the unit is m/s
        :return: The speed limit number, the unit is m/s.
        """
        speed_limit_num = int(self.sign_type[:-3])

        if self.sign_type[-3:] == "kmh":
            return speed_limit_num/3.6
        elif self.sign_type[-3:] == "mph":
            return speed_limit_num*0.44704
        else:
            raise Exception("No this unit {}".format(self.sign_type))


class RightOfWay(RegulatoryElement):
    def __init__(self, reg_id: int, reg_type: str, subtype: str, refers: list, ref_line: list, right_of_way: list,
                 yield_list: list):
        super().__init__(reg_id=reg_id, reg_type=reg_type, subtype=subtype)

        self.refers = refers
        self.ref_line = ref_line
        self.right_of_way = right_of_way
        self.yield_list = yield_list


class AllWayStop(RegulatoryElement):
    def __init__(self, reg_id: int, reg_type: str, subtype: str, refers: list, ref_line: list, yield_list: list):
        super().__init__(reg_id=reg_id, reg_type=reg_type, subtype=subtype)

        self.refers = refers
        self.ref_lines = ref_line
        self.yield_list = yield_list


class TrafficSign(RegulatoryElement):
    def __init__(self, reg_id: int, reg_type: str, subtype: str, ref_node_list: list):
        super().__init__(reg_id=reg_id, reg_type=reg_type, subtype=subtype)

        self.ref_node_list = ref_node_list
        self.sign_meaning = None

    def get_sign_meaning(self) -> str:
        """
        Parser the meaning of the sign.
        :return: The meaning of the sign, string type.
        """
        region_code = self.subtype[:2]
        sign = self.subtype[2:]

        if region_code == "de" or region_code == "DE":
            if sign == "215":
                # ????????????, ??????????????????: ??????????????????, ????????????????????????
                return "DE-Roundabout"
            elif sign == "205":
                # ???????????????, ????????????????????????????????????,????????????, ???????????????????????????????????????????????????, ???????????????????????????.
                return "DE-Yield"
            else:
                raise Exception("No this sign record: {}-{}".format(self.subtype, sign))
        elif region_code == "us" or region_code == "US":
            if sign == "R1-1":
                # ????????????, ??????????????????, ??????????????????
                return "US-Stop"
            elif sign == "R1-3P":
                # ?????????stop??????????????????,?????????????????????????????????Stop????????????3???,??????????????????,?????????
                return "US-AllWay"
            elif sign == "do_not_enter" or sign == "R5-1":
                # ????????????
                return "US-DoNotEnter"
            elif sign == "R3-5R":
                # ????????????
                return "US-RightTurnOnly"
            elif sign == "R5-1a":
                # ????????????
                return "US-WrongWay"
            elif sign == "R6-1L":
                # ???????????????
                return "US-OneWayLeft"
            elif sign == "R1-2":
                # yield ????????????
                return "US-Yield"
            elif sign == "W5-1":
                # road narrows
                return "US-RoadNarrows"
            elif sign == "R4-7":
                # keep right
                return "US-KeepRight"
            elif sign == "R4-8a":
                # keep left
                return "US-KeepLeft"
            elif sign == "R3-1":
                return "US-NoRightTurn"
            elif sign == "R3-2":
                return "US-NoLeftTurn"
            else:
                raise Exception("No this sign record: {}-{}".format(self.subtype, sign))
        else:
            raise Exception("No this region has been record: {}-{}".format(self.subtype, region_code))