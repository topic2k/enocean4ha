# -*- encoding: utf-8 -*-

from enum import IntEnum


# EnOceanSerialProtocol3.pdf / 12
class PACKET(IntEnum):
    RESERVED = 0x00
    # RADIO == RADIO_ERP1
    # Kept for backwards compatibility reasons, for example custom packet
    # generation shouldn't be affected...
    RADIO = 0x01
    RADIO_ERP1 = 0x01
    RESPONSE = 0x02
    RADIO_SUB_TEL = 0x03
    EVENT = 0x04
    COMMON_COMMAND = 0x05
    SMART_ACK_COMMAND = 0x06
    REMOTE_MAN_COMMAND = 0x07
    RADIO_MESSAGE = 0x09
    # RADIO_ADVANCED == RADIO_ERP2
    # Kept for backwards compatibility reasons
    RADIO_ADVANCED = 0x0A
    RADIO_ERP2 = 0x0A
    RADIO_802_15_4 = 0x10
    COMMAND_2_4 = 0x11


# EnOceanSerialProtocol3-1-1.pdf / 33
# noinspection PyPep8Naming
class COMMON_COMMAND(IntEnum):
    CO_RD_VERSION = 0x03
    CO_RD_IDBASE = 0x08


# EnOceanSerialProtocol3.pdf / 18
# noinspection PyPep8Naming
class RETURN_CODE(IntEnum):
    OK = 0x00
    ERROR = 0x01
    NOT_SUPPORTED = 0x02
    WRONG_PARAM = 0x03
    OPERATION_DENIED = 0x04


# EnOceanSerialProtocol3.pdf / 20
# noinspection PyPep8Naming
class EVENT_CODE(IntEnum):
    SA_RECLAIM_NOT_SUCCESFUL = 0x01
    SA_CONFIRM_LEARN = 0x02
    SA_LEARN_ACK = 0x03
    CO_READY = 0x04
    CO_EVENT_SECUREDEVICES = 0x05


# EnOcean_Equipment_Profiles_EEP_V2.61_public.pdf / 8
# noinspection PyPep8Naming
class RORG(IntEnum):
    UNDEFINED = 0x00
    RPS = 0xF6
    BS1 = 0xD5
    BS4 = 0xA5
    VLD = 0xD2
    MSC = 0xD1
    ADT = 0xA6
    SM_LRN_REQ = 0xC6
    SM_LRN_ANS = 0xC7
    SM_REC = 0xA7
    SYS_EX = 0xC5
    SEC = 0x30
    SEC_ENCAPS = 0x31
    SEC_MAN = 0x34
    SIGNAL = 0xD0
    UTE = 0xD4


# Results for message parsing
# noinspection PyPep8Naming
class PARSE_RESULT(IntEnum):
    OK = 0x00
    INCOMPLETE = 0x01
    CRC_MISMATCH = 0x03


# Data byte indexing
# Starts from the end, so works on messages of all length.
class DB0:
    BIT_0 = -1
    BIT_1 = -2
    BIT_2 = -3
    BIT_3 = -4
    BIT_4 = -5
    BIT_5 = -6
    BIT_6 = -7
    BIT_7 = -8


class DB1:
    BIT_0 = -9
    BIT_1 = -10
    BIT_2 = -11
    BIT_3 = -12
    BIT_4 = -13
    BIT_5 = -14
    BIT_6 = -15
    BIT_7 = -16


class DB2:
    BIT_0 = -17
    BIT_1 = -18
    BIT_2 = -19
    BIT_3 = -20
    BIT_4 = -21
    BIT_5 = -22
    BIT_6 = -23
    BIT_7 = -24


class DB3:
    BIT_0 = -25
    BIT_1 = -26
    BIT_2 = -27
    BIT_3 = -28
    BIT_4 = -29
    BIT_5 = -30
    BIT_6 = -31
    BIT_7 = -32


class DB4:
    BIT_0 = -33
    BIT_1 = -34
    BIT_2 = -35
    BIT_3 = -36
    BIT_4 = -37
    BIT_5 = -38
    BIT_6 = -39
    BIT_7 = -40


class DB5:
    BIT_0 = -41
    BIT_1 = -42
    BIT_2 = -43
    BIT_3 = -44
    BIT_4 = -45
    BIT_5 = -46
    BIT_6 = -47
    BIT_7 = -48


class DB6:
    BIT_0 = -49
    BIT_1 = -50
    BIT_2 = -51
    BIT_3 = -52
    BIT_4 = -53
    BIT_5 = -54
    BIT_6 = -55
    BIT_7 = -56


# https://enoceanwiki.atlassian.net/wiki/spaces/IEC/pages/260669482/EnOcean+Alliance+Manufacturer+IDs
MANUFACTURES: dict[int, str] = {
    0x00: "Reserved",
    0x01: "Peha",
    0x02: "Thermokon",
    0x03: "Servodan",
    0x04: "Echoflex Solutions",
    0x05: "Awag Elektrotechnik Ag or Omnio Ag",
    # 0x05: "Awag Elektrotechnik Ag",
    # 0x05: "Omnio Ag",
    0x06: "Hardmeier Electronics",
    0x07: "Regulvar Inc",
    0x08: "Ad Hoc Electronics",
    0x09: "Distech Controls",
    0x0A: "Kieback And Peter",
    0x0B: "EnOcean",
    0x0C: "Probare or Vicos Gmbh",
    # 0x0C: "Probare",
    # 0x0C: "Vicos Gmbh",
    0x0D: "Eltako",
    0x0E: "Leviton",
    0x0F: "Honeywell",
    0x10: "Spartan Peripheral Devices",
    0x11: "Siemens",
    0x12: "T Mac",
    0x13: "Reliable Controls Corporation",
    0x14: "Elsner Elektronik Gmbh",
    0x15: "Diehl Controls",
    0x16: "Bsc Computer",
    0x17: "S And S Regeltechnik Gmbh",
    0x18: "Masco Corporation or Zeno Controls",
    # 0x18: "Masco Corporation",
    # 0x18: "Zeno Controls",
    0x19: "Intesis Software Sl",
    0x1A: "Viessmann",
    0x1B: "Lutuo Technology",
    0x1C: "Can2Go",
    0x1D: "Sauter",
    0x1E: "Boot Up",
    0x1F: "Osram Sylvania",
    0x20: "Unotech",
    0x21: "Delta Controls Inc",
    0x22: "Unitronic Ag",
    0x23: "Nanosense",
    0x24: "The S4 Group",
    0x25: "Msr Solutions or Veissmann Hausatomation Gmbh",
    # 0x25: "Msr Solutions",
    # 0x25: "Veissmann Hausatomation Gmbh",
    0x26: "GE",
    0x27: "Maico",
    0x28: "Ruskin Company",
    0x29: "Magnum Energy Solutions",
    0x2A: "KMC Controls",
    0x2B: "Ecologix Controls",
    0x2C: "Trio 2 Sys",
    0x2D: "Afriso Euro Index",
    0x2E: "Waldmann Gmbh",
    0x30: "Nec Platforms Ltd",
    0x31: "Itec Corporation",
    0x32: "Simicx Co Ltd",
    0x33: "Permundo Gmbh",
    0x34: "Eurotronic Technology Gmbh",
    0x35: "Art Japan Co Ltd",
    0x36: "Tiansu Automation Control Syste Co Ltd",
    0x37: "Weinzierl Engineering Gmbh",
    0x38: "Gruppo Giordano Idea Spa",
    0x39: "Alphaeos Ag",
    0x3A: "Tag Technologies",
    0x3B: "Wattstopper",
    0x3C: "Pressac Communications Ltd",
    0x3E: "Giga Concept",
    0x3F: "Sensortec",
    0x40: "Jaeger Direkt",
    0x41: "Air System Components Inc",
    0x42: "Ermine Corp",
    0x43: "Soda Gmbh",
    0x44: "Eke Automation",
    0x45: "Holter Regelarmutren",
    0x46: "ID RF",
    0x47: "Deuta Controls Gmbh",
    0x48: "Ewattch",
    0x49: "Micropelt",
    0x4A: "Caleffi Spa",
    0x4B: "Digital Concepts",
    0x4C: "Emerson Climate Technologies",
    0x4D: "Adee Electronic",
    0x4E: "Altecon",
    0x4F: "Nanjing Putian Telecommunications",
    0x50: "Terralux",
    0x51: "Menred",
    0x52: "Iexergy Gmbh",
    0x53: "Oventrop Gmbh",
    0x54: "Building Automation Products Inc",
    0x55: "Functional Devices Inc",
    0x56: "Ogga",
    0x57: "Itho Daalderop",
    0x58: "Resol",
    0x59: "Advanced Devices",
    0x5A: "Autani Lcc",
    0x5B: "Dr Riedel Gmbh",
    0x5C: "Hoppe Holding Ag",
    0x5D: "Siegenia Aubi Kg",
    0x5E: "Adeo Services",
    0x5F: "Eimsig Efp Gmbh",
    0x60: "Vimar Spa",
    0x61: "Glen Dimlax Gmbh",
    0x62: "Pmdm Gmbh",
    0x63: "Hubbel Lightning",
    0x64: "Debflex",
    0x65: "Perifactory Sensorsystems",
    0x66: "Watty Corp",
    0x67: "Wago Kontakttechnik",
    0x68: "Kessel",
    0x69: "Aug Winkhaus",
    0x6A: "Decelect",
    0x6B: "Mst Industries",
    0x6C: "Becker Antriebe",
    0x6D: "Nexelec",
    0x6E: "Wieland Electric",
    0x6F: "Avidsen",
    0x70: "Cws Boco International",
    0x71: "Roto Frank",
    0x72: "Alm Contorls",
    0x73: "Tommaso Technologies",
    0x74: "Rehau",
    0x75: "Inaba Denki Sangyo Co Lt",
    0x76: "Hager Controls Sas",
    0xFF: "Multiple",
}
