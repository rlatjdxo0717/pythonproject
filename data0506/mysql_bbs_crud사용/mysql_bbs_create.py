import db연결.mysql_bbs.bbs_dao as db

id = input('아이디를 입력하세요.')
title = input('제목을 입력하세요.')
content = input('내용을 입력하세요.')
writer = input('작성자를 입력하세요.')

db.create(id, title, content, writer)
