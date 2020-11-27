from imp import cursor, connection

#cursor.execute('create database telegram_bot_1')
#connection.commit()

cursor.execute('CREATE TABLE const_info(id INT AUTO_INCREMENT PRIMARY KEY, data TEXT)')
connection.commit()

cursor.execute('CREATE TABLE reviews(id INT AUTO_INCREMENT PRIMARY KEY, data TEXT)')
connection.commit()


