from codes import convertToDecimal, convertFromDecimal

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

def test_convertFromDecimal():
  assert (convertFromDecimal(1833, 2)) == "11100101001"
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

test_convertToDecimal()
test_convertFromDecimal()
print("passed!")