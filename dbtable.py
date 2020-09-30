import mysql.connector

dbtble= mysql.connector.connect(
    host="localhost",
    user="root",
    password="webcreationz@1234",
    database ="db1"
)
mycursor = dbtble.cursor()
data ="INSERT INTO BMIHEIGHT (ftin, inches, centimeters) VALUES(%s,%s,%s)"
dval = [
  ('5’0”', '60in','152.40cm'),
  (' 5’1”', '61 in','154.94'),
  ('5’2”', '62in','157.48cm'),
  ('5’3”', '63in','160.02cm'),
  ('5’4”', '64in','162.56cm'),
  ('5’5”', '65 in','165.10cm'),
  ('5’6”', 'S 66 in','167.74cm'),
  ('5’7”', '67 in','170.18cm'),
  ('5’8”', '68 in','172.72cm'),
  ('5’9”', '69in','175.26cm'),
  ('5’10”', '70in','177.80cm'),
  ('5’11”', '71in','180.34cm'),
  ('6’0”', '72in','182.88cm'),
  ('6’1”', '73in', '185.45cm'),
  ('6’2”', '74in', '187.96cm'),
  ('6’3”', '75in', '190.50cm'),
  ('6’4”', '76in', '193.04cm'),
  ('6’5”', '77in', '195.58cm'),
  ('6’6”', '78in', '198.12cm'),
  ('6’7”', '79in', '200.66cm'),
  ('6’8”', '80in', '203.20cm'),
  ('6’9”', '81in', '205.74cm'),
  ('6’10”', '82in', '208.28cm'),
  ('6’11”', '83in', '210.82cm'),
  ('7’0”', '84in', '213.36cm'),
  ('7’1”', '85in', '215.90cm'),
  ('7’2”', '86in', '218.44cm')

]
mycursor.executemany(data,dval)
dbtble.commit()
print(dbtble.connection_id)