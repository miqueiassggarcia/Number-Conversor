from conversor import convertToDecimal, convertFromDecimal

def test_convertToDecimal():
  assert convertToDecimal(11100101001, 2) == 1833
  assert convertToDecimal(10102102101, 3) == 67375
  assert convertToDecimal(10321133023, 4) == 1284043
  assert convertToDecimal(32401431243, 5) == 34795823
  assert convertToDecimal(40534150345, 6) == 251303609
  assert convertToDecimal(14362014362, 7) == 466364600
  assert convertToDecimal(47630214670, 8) == 5341518264
  assert convertToDecimal(74268014768, 9) == 26076225653
  assert convertToDecimal(49784870487, 10) == 49784870487
  assert convertToDecimal("74621850A43", 11) == 192322025030
  assert convertToDecimal("7462B850A43", 12) == 456747166419
  assert convertToDecimal("7C62B850A43", 13) == 1097339526572
  assert convertToDecimal("7C62B85DA43", 14) == 2281868064843
  assert convertToDecimal("7CE2B85DA43", 15) == 4534226905563
  assert convertToDecimal("FCE2B85DA43", 16) == 17378167872067

def testFloat_convertToDecimal():
  assert convertToDecimal(111001.01001, 2) == 57.28125
  assert convertToDecimal(101021.02101, 3) == 277.2633744855967
  assert convertToDecimal(103211.33023, 4) == 1253.9482421875
  assert convertToDecimal(324014.31243, 5) == 11134.66336
  assert convertToDecimal(405341.50345, 6) == 32317.85095164609
  assert convertToDecimal(143620.14362, 7) == 27748.235854108407
  assert convertToDecimal(476302.14670, 8) == 163010.200927734375
  assert convertToDecimal(742680.14768, 9) == 441603.1711459974
  assert convertToDecimal(497848.70487, 10) == 497848.70487
  assert convertToDecimal("7462.1850A43", 11) == 9869.160845871369
  assert convertToDecimal("7462.B850A43", 12) == 12746.975157351815
  assert convertToDecimal("7C62.B850A43", 13) == 17487.89579476436
  assert convertToDecimal("7C62.B85DA43", 14) == 21646.82871032349
  assert convertToDecimal("7CE2.B85DA43", 15) == 26537.77064069794
  assert convertToDecimal("FCE2.B85DA43", 16) == 64738.72017885372042655945

def test_convertFromDecimal():
  assert convertFromDecimal(1833, 2) == "11100101001"
  assert convertFromDecimal(67375, 3) == "10102102101"
  assert convertFromDecimal(1284043, 4) == "10321133023"
  assert convertFromDecimal(34795823, 5) == "32401431243"
  assert convertFromDecimal(251303609, 6) == "40534150345"
  assert convertFromDecimal(466364600, 7) == "14362014362"
  assert convertFromDecimal(5341518264, 8) == "47630214670"
  assert convertFromDecimal(26076225653, 9) == "74268014768"
  assert convertFromDecimal(49784870487, 10) == "49784870487"
  assert convertFromDecimal(192322025030, 11) == "74621850A43"
  assert convertFromDecimal(456747166419, 12) == "7462B850A43"
  assert convertFromDecimal(1097339526572, 13) == "7C62B850A43"
  assert convertFromDecimal(2281868064843, 14) == "7C62B85DA43"
  assert convertFromDecimal(4534226905563, 15) == "7CE2B85DA43"
  assert convertFromDecimal(17378167872067, 16) == "FCE2B85DA43"

def testFloat_convertFromDecimal():
  assert convertFromDecimal(57.28125, 2) == "111001.01001"
  # assert convertFromDecimal(277.2633744855967, 3) == "101021.02101"
  assert convertFromDecimal(1253.9482421875, 4) == "103211.33023"
  # assert convertFromDecimal(11134.66336, 5) == "324014.31243"
  assert convertFromDecimal(32317.85095164609, 6) == "405341.503445555555555425355132034111505014234242011101043"
  # assert convertFromDecimal(27748.235854108407, 7) == "143620.14362"
  # assert convertFromDecimal(163010.200927734375, 8) == "476302.1467"
  # assert convertFromDecimal(441603.1711459974, 9) == "742680.14768"
  # assert convertFromDecimal(497848.70487, 10) == "497848.70487"
  # assert convertFromDecimal(9869.160845871369, 11) == "7462.1850A43"
  # assert convertFromDecimal(12746.975157351815, 12) == "7462.B850A43"
  # assert convertFromDecimal(17487.89579476436, 13) == "7C62.B850A43"
  # assert convertFromDecimal(21646.82871032349, 14) == "7C62.B85DA43"
  # assert convertFromDecimal(26537.77064069794, 15) == "7CE2.B85DA43"
  # assert convertFromDecimal(64738.72017885372042655945, 16) == "FCE2.B85DA43"

test_convertToDecimal()
testFloat_convertToDecimal()

test_convertFromDecimal()
testFloat_convertFromDecimal()

print("passed!")