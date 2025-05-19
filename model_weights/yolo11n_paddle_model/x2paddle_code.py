import paddle
import math
from x2paddle.op_mapper.pytorch2paddle import pytorch_custom_layer as x2paddle_nn

class DetectionModel(paddle.nn.Layer):
    def __init__(self):
        super(DetectionModel, self).__init__()
        self.conv2d0 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=16, kernel_size=(3, 3), in_channels=3)
        self.silu0 = paddle.nn.Silu()
        self.conv2d1 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=32, kernel_size=(3, 3), in_channels=16)
        self.silu1 = paddle.nn.Silu()
        self.conv2d2 = paddle.nn.Conv2D(out_channels=32, kernel_size=(1, 1), in_channels=32)
        self.silu2 = paddle.nn.Silu()
        self.conv2d3 = paddle.nn.Conv2D(padding=1, out_channels=8, kernel_size=(3, 3), in_channels=16)
        self.silu3 = paddle.nn.Silu()
        self.conv2d4 = paddle.nn.Conv2D(padding=1, out_channels=16, kernel_size=(3, 3), in_channels=8)
        self.silu4 = paddle.nn.Silu()
        self.conv2d5 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=48)
        self.silu5 = paddle.nn.Silu()
        self.conv2d6 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu6 = paddle.nn.Silu()
        self.conv2d7 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=64)
        self.silu7 = paddle.nn.Silu()
        self.conv2d8 = paddle.nn.Conv2D(padding=1, out_channels=16, kernel_size=(3, 3), in_channels=32)
        self.silu8 = paddle.nn.Silu()
        self.conv2d9 = paddle.nn.Conv2D(padding=1, out_channels=32, kernel_size=(3, 3), in_channels=16)
        self.silu9 = paddle.nn.Silu()
        self.conv2d10 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=96)
        self.silu10 = paddle.nn.Silu()
        self.conv2d11 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=128, kernel_size=(3, 3), in_channels=128)
        self.silu11 = paddle.nn.Silu()
        self.conv2d12 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=128)
        self.silu12 = paddle.nn.Silu()
        self.conv2d13 = paddle.nn.Conv2D(out_channels=32, kernel_size=(1, 1), in_channels=64)
        self.silu13 = paddle.nn.Silu()
        self.conv2d14 = paddle.nn.Conv2D(padding=1, out_channels=32, kernel_size=(3, 3), in_channels=32)
        self.silu14 = paddle.nn.Silu()
        self.conv2d15 = paddle.nn.Conv2D(padding=1, out_channels=32, kernel_size=(3, 3), in_channels=32)
        self.silu15 = paddle.nn.Silu()
        self.conv2d16 = paddle.nn.Conv2D(padding=1, out_channels=32, kernel_size=(3, 3), in_channels=32)
        self.silu16 = paddle.nn.Silu()
        self.conv2d17 = paddle.nn.Conv2D(padding=1, out_channels=32, kernel_size=(3, 3), in_channels=32)
        self.silu17 = paddle.nn.Silu()
        self.conv2d18 = paddle.nn.Conv2D(out_channels=32, kernel_size=(1, 1), in_channels=64)
        self.silu18 = paddle.nn.Silu()
        self.conv2d19 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=64)
        self.silu19 = paddle.nn.Silu()
        self.conv2d20 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=192)
        self.silu20 = paddle.nn.Silu()
        self.conv2d21 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=256, kernel_size=(3, 3), in_channels=128)
        self.silu21 = paddle.nn.Silu()
        self.conv2d22 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=256)
        self.silu22 = paddle.nn.Silu()
        self.conv2d23 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=128)
        self.silu23 = paddle.nn.Silu()
        self.conv2d24 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu24 = paddle.nn.Silu()
        self.conv2d25 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu25 = paddle.nn.Silu()
        self.conv2d26 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu26 = paddle.nn.Silu()
        self.conv2d27 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu27 = paddle.nn.Silu()
        self.conv2d28 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=128)
        self.silu28 = paddle.nn.Silu()
        self.conv2d29 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=128)
        self.silu29 = paddle.nn.Silu()
        self.conv2d30 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=384)
        self.silu30 = paddle.nn.Silu()
        self.conv2d31 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=256)
        self.silu31 = paddle.nn.Silu()
        self.pool2d0 = paddle.nn.MaxPool2D(kernel_size=[5, 5], stride=1, padding=2)
        self.pool2d1 = paddle.nn.MaxPool2D(kernel_size=[5, 5], stride=1, padding=2)
        self.pool2d2 = paddle.nn.MaxPool2D(kernel_size=[5, 5], stride=1, padding=2)
        self.conv2d32 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=512)
        self.silu32 = paddle.nn.Silu()
        self.conv2d33 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=256)
        self.silu33 = paddle.nn.Silu()
        self.conv2d34 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=128)
        self.softmax0 = paddle.nn.Softmax()
        self.conv2d35 = paddle.nn.Conv2D(padding=1, groups=128, out_channels=128, kernel_size=(3, 3), in_channels=128)
        self.conv2d36 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=128)
        self.conv2d37 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=128)
        self.silu34 = paddle.nn.Silu()
        self.conv2d38 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=256)
        self.conv2d39 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=256)
        self.silu35 = paddle.nn.Silu()
        self.conv2d40 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=384)
        self.silu36 = paddle.nn.Silu()
        self.conv2d41 = paddle.nn.Conv2D(padding=1, out_channels=32, kernel_size=(3, 3), in_channels=64)
        self.silu37 = paddle.nn.Silu()
        self.conv2d42 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=32)
        self.silu38 = paddle.nn.Silu()
        self.conv2d43 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=192)
        self.silu39 = paddle.nn.Silu()
        self.conv2d44 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=256)
        self.silu40 = paddle.nn.Silu()
        self.conv2d45 = paddle.nn.Conv2D(padding=1, out_channels=16, kernel_size=(3, 3), in_channels=32)
        self.silu41 = paddle.nn.Silu()
        self.conv2d46 = paddle.nn.Conv2D(padding=1, out_channels=32, kernel_size=(3, 3), in_channels=16)
        self.silu42 = paddle.nn.Silu()
        self.conv2d47 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=96)
        self.silu43 = paddle.nn.Silu()
        self.conv2d48 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu44 = paddle.nn.Silu()
        self.conv2d49 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=192)
        self.silu45 = paddle.nn.Silu()
        self.conv2d50 = paddle.nn.Conv2D(padding=1, out_channels=32, kernel_size=(3, 3), in_channels=64)
        self.silu46 = paddle.nn.Silu()
        self.conv2d51 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=32)
        self.silu47 = paddle.nn.Silu()
        self.conv2d52 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=192)
        self.silu48 = paddle.nn.Silu()
        self.conv2d53 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=128, kernel_size=(3, 3), in_channels=128)
        self.silu49 = paddle.nn.Silu()
        self.conv2d54 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=384)
        self.silu50 = paddle.nn.Silu()
        self.conv2d55 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=128)
        self.silu51 = paddle.nn.Silu()
        self.conv2d56 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu52 = paddle.nn.Silu()
        self.conv2d57 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu53 = paddle.nn.Silu()
        self.conv2d58 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu54 = paddle.nn.Silu()
        self.conv2d59 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu55 = paddle.nn.Silu()
        self.conv2d60 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=128)
        self.silu56 = paddle.nn.Silu()
        self.conv2d61 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=128)
        self.silu57 = paddle.nn.Silu()
        self.conv2d62 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=384)
        self.silu58 = paddle.nn.Silu()
        self.x868 = self.create_parameter(dtype='float32', shape=(1, 8400), default_initializer=paddle.nn.initializer.Constant(value=0.0))
        self.conv2d63 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu59 = paddle.nn.Silu()
        self.conv2d64 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu60 = paddle.nn.Silu()
        self.conv2d65 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=64)
        self.conv2d66 = paddle.nn.Conv2D(padding=1, groups=64, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu61 = paddle.nn.Silu()
        self.conv2d67 = paddle.nn.Conv2D(out_channels=80, kernel_size=(1, 1), in_channels=64)
        self.silu62 = paddle.nn.Silu()
        self.conv2d68 = paddle.nn.Conv2D(padding=1, groups=80, out_channels=80, kernel_size=(3, 3), in_channels=80)
        self.silu63 = paddle.nn.Silu()
        self.conv2d69 = paddle.nn.Conv2D(out_channels=80, kernel_size=(1, 1), in_channels=80)
        self.silu64 = paddle.nn.Silu()
        self.conv2d70 = paddle.nn.Conv2D(out_channels=80, kernel_size=(1, 1), in_channels=80)
        self.conv2d71 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=128)
        self.silu65 = paddle.nn.Silu()
        self.conv2d72 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu66 = paddle.nn.Silu()
        self.conv2d73 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=64)
        self.conv2d74 = paddle.nn.Conv2D(padding=1, groups=128, out_channels=128, kernel_size=(3, 3), in_channels=128)
        self.silu67 = paddle.nn.Silu()
        self.conv2d75 = paddle.nn.Conv2D(out_channels=80, kernel_size=(1, 1), in_channels=128)
        self.silu68 = paddle.nn.Silu()
        self.conv2d76 = paddle.nn.Conv2D(padding=1, groups=80, out_channels=80, kernel_size=(3, 3), in_channels=80)
        self.silu69 = paddle.nn.Silu()
        self.conv2d77 = paddle.nn.Conv2D(out_channels=80, kernel_size=(1, 1), in_channels=80)
        self.silu70 = paddle.nn.Silu()
        self.conv2d78 = paddle.nn.Conv2D(out_channels=80, kernel_size=(1, 1), in_channels=80)
        self.conv2d79 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=256)
        self.silu71 = paddle.nn.Silu()
        self.conv2d80 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu72 = paddle.nn.Silu()
        self.conv2d81 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=64)
        self.conv2d82 = paddle.nn.Conv2D(padding=1, groups=256, out_channels=256, kernel_size=(3, 3), in_channels=256)
        self.silu73 = paddle.nn.Silu()
        self.conv2d83 = paddle.nn.Conv2D(out_channels=80, kernel_size=(1, 1), in_channels=256)
        self.silu74 = paddle.nn.Silu()
        self.conv2d84 = paddle.nn.Conv2D(padding=1, groups=80, out_channels=80, kernel_size=(3, 3), in_channels=80)
        self.silu75 = paddle.nn.Silu()
        self.conv2d85 = paddle.nn.Conv2D(out_channels=80, kernel_size=(1, 1), in_channels=80)
        self.silu76 = paddle.nn.Silu()
        self.conv2d86 = paddle.nn.Conv2D(out_channels=80, kernel_size=(1, 1), in_channels=80)
        self.softmax1 = paddle.nn.Softmax(axis=1)
        self.conv2d87 = paddle.nn.Conv2D(out_channels=1, kernel_size=(1, 1), bias_attr=False, in_channels=16)
        self.x1157 = self.create_parameter(dtype='float32', shape=(1, 2, 8400), default_initializer=paddle.nn.initializer.Constant(value=0.0))
        self.sigmoid0 = paddle.nn.Sigmoid()

    def forward(self, x0):
        x47 = self.conv2d0(x0)
        x48 = self.silu0(x47)
        x59 = self.conv2d1(x48)
        x60 = self.silu1(x59)
        x75 = self.conv2d2(x60)
        x76 = self.silu2(x75)
        x78 = paddle.split(x=x76, num_or_sections=2, axis=1)
        x79, x80 = x78
        x90 = self.conv2d3(x80)
        x91 = self.silu3(x90)
        x99 = self.conv2d4(x91)
        x100 = self.silu4(x99)
        x101 = x80 + x100
        x102 = [x79, x80, x101]
        x103 = paddle.concat(x=x102, axis=1)
        x111 = self.conv2d5(x103)
        x112 = self.silu5(x111)
        x123 = self.conv2d6(x112)
        x124 = self.silu6(x123)
        x139 = self.conv2d7(x124)
        x140 = self.silu7(x139)
        x142 = paddle.split(x=x140, num_or_sections=2, axis=1)
        x143, x144 = x142
        x154 = self.conv2d8(x144)
        x155 = self.silu8(x154)
        x163 = self.conv2d9(x155)
        x164 = self.silu9(x163)
        x165 = x144 + x164
        x166 = [x143, x144, x165]
        x167 = paddle.concat(x=x166, axis=1)
        x175 = self.conv2d10(x167)
        x176 = self.silu10(x175)
        x187 = self.conv2d11(x176)
        x188 = self.silu11(x187)
        x203 = self.conv2d12(x188)
        x204 = self.silu12(x203)
        x206 = paddle.split(x=x204, num_or_sections=2, axis=1)
        x207, x208 = x206
        x220 = self.conv2d13(x208)
        x221 = self.silu13(x220)
        x233 = self.conv2d14(x221)
        x234 = self.silu14(x233)
        x242 = self.conv2d15(x234)
        x243 = self.silu15(x242)
        x244 = x221 + x243
        x254 = self.conv2d16(x244)
        x255 = self.silu16(x254)
        x263 = self.conv2d17(x255)
        x264 = self.silu17(x263)
        x265 = x244 + x264
        x273 = self.conv2d18(x208)
        x274 = self.silu18(x273)
        x275 = [x265, x274]
        x276 = paddle.concat(x=x275, axis=1)
        x284 = self.conv2d19(x276)
        x285 = self.silu19(x284)
        x286 = [x207, x208, x285]
        x287 = paddle.concat(x=x286, axis=1)
        x295 = self.conv2d20(x287)
        x296 = self.silu20(x295)
        x307 = self.conv2d21(x296)
        x308 = self.silu21(x307)
        x323 = self.conv2d22(x308)
        x324 = self.silu22(x323)
        x326 = paddle.split(x=x324, num_or_sections=2, axis=1)
        x327, x328 = x326
        x340 = self.conv2d23(x328)
        x341 = self.silu23(x340)
        x353 = self.conv2d24(x341)
        x354 = self.silu24(x353)
        x362 = self.conv2d25(x354)
        x363 = self.silu25(x362)
        x364 = x341 + x363
        x374 = self.conv2d26(x364)
        x375 = self.silu26(x374)
        x383 = self.conv2d27(x375)
        x384 = self.silu27(x383)
        x385 = x364 + x384
        x393 = self.conv2d28(x328)
        x394 = self.silu28(x393)
        x395 = [x385, x394]
        x396 = paddle.concat(x=x395, axis=1)
        x404 = self.conv2d29(x396)
        x405 = self.silu29(x404)
        x406 = [x327, x328, x405]
        x407 = paddle.concat(x=x406, axis=1)
        x415 = self.conv2d30(x407)
        x416 = self.silu30(x415)
        x429 = self.conv2d31(x416)
        x430 = self.silu31(x429)
        x435 = self.pool2d0(x430)
        x440 = self.pool2d1(x435)
        x445 = self.pool2d2(x440)
        x446 = [x430, x435, x440, x445]
        x447 = paddle.concat(x=x446, axis=1)
        x455 = self.conv2d32(x447)
        x456 = self.silu32(x455)
        x458 = -2
        x459 = -1
        x460 = 0.1767766952966369
        x476 = self.conv2d33(x456)
        x477 = self.silu33(x476)
        x479 = paddle.split(x=x477, num_or_sections=2, axis=1)
        x480, x481 = x479
        x495 = self.conv2d34(x481)
        x497 = paddle.reshape(x=x495, shape=[1, 2, 128, 400])
        x499 = paddle.split(x=x497, num_or_sections=[32, 32, 64], axis=2)
        x500, x501, x502 = x499
        x503_shape = x500.shape
        x503_len = len(x503_shape)
        x503_list = []
        for i in range(x503_len):
            x503_list.append(i)
        if x458 < 0:
            x458_new = x458 + x503_len
        else:
            x458_new = x458
        if x459 < 0:
            x459_new = x459 + x503_len
        else:
            x459_new = x459
        x503_list[x458_new] = x459_new
        x503_list[x459_new] = x458_new
        x503 = paddle.transpose(x=x500, perm=x503_list)
        x504 = paddle.matmul(x=x503, y=x501)
        x505 = x504 * x460
        x506 = self.softmax0(x505)
        x507_shape = x506.shape
        x507_len = len(x507_shape)
        x507_list = []
        for i in range(x507_len):
            x507_list.append(i)
        if x458 < 0:
            x458_new = x458 + x507_len
        else:
            x458_new = x458
        if x459 < 0:
            x459_new = x459 + x507_len
        else:
            x459_new = x459
        x507_list[x458_new] = x459_new
        x507_list[x459_new] = x458_new
        x507 = paddle.transpose(x=x506, perm=x507_list)
        x508 = paddle.matmul(x=x502, y=x507)
        x510 = paddle.reshape(x=x508, shape=[1, 128, 20, 20])
        x512 = paddle.reshape(x=x502, shape=[1, 128, 20, 20])
        x520 = self.conv2d35(x512)
        x521 = x510 + x520
        x529 = self.conv2d36(x521)
        x530 = x481 + x529
        x540 = self.conv2d37(x530)
        x541 = self.silu34(x540)
        x549 = self.conv2d38(x541)
        x550 = x530 + x549
        x551 = [x480, x550]
        x552 = paddle.concat(x=x551, axis=1)
        x560 = self.conv2d39(x552)
        x561 = self.silu35(x560)
        x563 = [2.0, 2.0]
        x564 = paddle.nn.functional.interpolate(x=x561, scale_factor=x563, mode='nearest')
        x566 = [x564, x296]
        x567 = paddle.concat(x=x566, axis=1)
        x582 = self.conv2d40(x567)
        x583 = self.silu36(x582)
        x585 = paddle.split(x=x583, num_or_sections=2, axis=1)
        x586, x587 = x585
        x597 = self.conv2d41(x587)
        x598 = self.silu37(x597)
        x606 = self.conv2d42(x598)
        x607 = self.silu38(x606)
        x608 = x587 + x607
        x609 = [x586, x587, x608]
        x610 = paddle.concat(x=x609, axis=1)
        x618 = self.conv2d43(x610)
        x619 = self.silu39(x618)
        x621 = [2.0, 2.0]
        x622 = paddle.nn.functional.interpolate(x=x619, scale_factor=x621, mode='nearest')
        x624 = [x622, x176]
        x625 = paddle.concat(x=x624, axis=1)
        x640 = self.conv2d44(x625)
        x641 = self.silu40(x640)
        x643 = paddle.split(x=x641, num_or_sections=2, axis=1)
        x644, x645 = x643
        x655 = self.conv2d45(x645)
        x656 = self.silu41(x655)
        x664 = self.conv2d46(x656)
        x665 = self.silu42(x664)
        x666 = x645 + x665
        x667 = [x644, x645, x666]
        x668 = paddle.concat(x=x667, axis=1)
        x676 = self.conv2d47(x668)
        x677 = self.silu43(x676)
        x688 = self.conv2d48(x677)
        x689 = self.silu44(x688)
        x691 = [x689, x619]
        x692 = paddle.concat(x=x691, axis=1)
        x707 = self.conv2d49(x692)
        x708 = self.silu45(x707)
        x710 = paddle.split(x=x708, num_or_sections=2, axis=1)
        x711, x712 = x710
        x722 = self.conv2d50(x712)
        x723 = self.silu46(x722)
        x731 = self.conv2d51(x723)
        x732 = self.silu47(x731)
        x733 = x712 + x732
        x734 = [x711, x712, x733]
        x735 = paddle.concat(x=x734, axis=1)
        x743 = self.conv2d52(x735)
        x744 = self.silu48(x743)
        x755 = self.conv2d53(x744)
        x756 = self.silu49(x755)
        x758 = [x756, x561]
        x759 = paddle.concat(x=x758, axis=1)
        x774 = self.conv2d54(x759)
        x775 = self.silu50(x774)
        x777 = paddle.split(x=x775, num_or_sections=2, axis=1)
        x778, x779 = x777
        x791 = self.conv2d55(x779)
        x792 = self.silu51(x791)
        x804 = self.conv2d56(x792)
        x805 = self.silu52(x804)
        x813 = self.conv2d57(x805)
        x814 = self.silu53(x813)
        x815 = x792 + x814
        x825 = self.conv2d58(x815)
        x826 = self.silu54(x825)
        x834 = self.conv2d59(x826)
        x835 = self.silu55(x834)
        x836 = x815 + x835
        x844 = self.conv2d60(x779)
        x845 = self.silu56(x844)
        x846 = [x836, x845]
        x847 = paddle.concat(x=x846, axis=1)
        x855 = self.conv2d61(x847)
        x856 = self.silu57(x855)
        x857 = [x778, x779, x856]
        x858 = paddle.concat(x=x857, axis=1)
        x866 = self.conv2d62(x858)
        x867 = self.silu58(x866)
        x868 = self.x868
        x869 = 2
        x871 = 2
        x876 = 1
        x902 = self.conv2d63(x677)
        x903 = self.silu59(x902)
        x911 = self.conv2d64(x903)
        x912 = self.silu60(x911)
        x919 = self.conv2d65(x912)
        x932 = self.conv2d66(x677)
        x933 = self.silu61(x932)
        x941 = self.conv2d67(x933)
        x942 = self.silu62(x941)
        x952 = self.conv2d68(x942)
        x953 = self.silu63(x952)
        x961 = self.conv2d69(x953)
        x962 = self.silu64(x961)
        x969 = self.conv2d70(x962)
        x970 = [x919, x969]
        x971 = paddle.concat(x=x970, axis=1)
        x982 = self.conv2d71(x744)
        x983 = self.silu65(x982)
        x991 = self.conv2d72(x983)
        x992 = self.silu66(x991)
        x999 = self.conv2d73(x992)
        x1012 = self.conv2d74(x744)
        x1013 = self.silu67(x1012)
        x1021 = self.conv2d75(x1013)
        x1022 = self.silu68(x1021)
        x1032 = self.conv2d76(x1022)
        x1033 = self.silu69(x1032)
        x1041 = self.conv2d77(x1033)
        x1042 = self.silu70(x1041)
        x1049 = self.conv2d78(x1042)
        x1050 = [x999, x1049]
        x1051 = paddle.concat(x=x1050, axis=1)
        x1062 = self.conv2d79(x867)
        x1063 = self.silu71(x1062)
        x1071 = self.conv2d80(x1063)
        x1072 = self.silu72(x1071)
        x1079 = self.conv2d81(x1072)
        x1092 = self.conv2d82(x867)
        x1093 = self.silu73(x1092)
        x1101 = self.conv2d83(x1093)
        x1102 = self.silu74(x1101)
        x1112 = self.conv2d84(x1102)
        x1113 = self.silu75(x1112)
        x1121 = self.conv2d85(x1113)
        x1122 = self.silu76(x1121)
        x1129 = self.conv2d86(x1122)
        x1130 = [x1079, x1129]
        x1131 = paddle.concat(x=x1130, axis=1)
        x1133 = paddle.reshape(x=x971, shape=[1, 144, -1])
        x1135 = paddle.reshape(x=x1051, shape=[1, 144, -1])
        x1137 = paddle.reshape(x=x1131, shape=[1, 144, -1])
        x1138 = [x1133, x1135, x1137]
        x1139 = paddle.concat(x=x1138, axis=2)
        x1141 = paddle.split(x=x1139, num_or_sections=[64, 80], axis=1)
        x1142, x1143 = x1141
        x1146 = paddle.reshape(x=x1142, shape=[1, 4, 16, 8400])
        x1147_shape = x1146.shape
        x1147_len = len(x1147_shape)
        x1147_list = []
        for i in range(x1147_len):
            x1147_list.append(i)
        if x871 < 0:
            x871_new = x871 + x1147_len
        else:
            x871_new = x871
        if x876 < 0:
            x876_new = x876 + x1147_len
        else:
            x876_new = x876
        x1147_list[x871_new] = x876_new
        x1147_list[x876_new] = x871_new
        x1147 = paddle.transpose(x=x1146, perm=x1147_list)
        x1148 = self.softmax1(x1147)
        x1154 = self.conv2d87(x1148)
        x1156 = paddle.reshape(x=x1154, shape=[1, 4, 8400])
        x1157 = self.x1157
        x1158 = paddle.split(x=x1156, num_or_sections=2, axis=1)
        x1159, x1160 = x1158
        x1161 = x1157 - x1159
        x1162 = x1157 + x1160
        x1163 = x1161 + x1162
        x1164 = x1163 / x869
        x1165 = x1162 - x1161
        x1166 = [x1164, x1165]
        x1167 = paddle.concat(x=x1166, axis=1)
        x1168 = x1167 * x868
        x1169 = self.sigmoid0(x1143)
        x1170 = [x1168, x1169]
        x1171 = paddle.concat(x=x1170, axis=1)
        return x1171

def main(x0):
    # There are 1 inputs.
    # x0: shape-[1, 3, 640, 640], type-float32.
    paddle.disable_static()
    params = paddle.load(r'/home/prane/Documents/rpi5-yolo-nn/yolo11n_paddle_model/model.pdparams')
    model = DetectionModel()
    model.set_dict(params, use_structured_name=True)
    model.eval()
    out = model(x0)
    return out
