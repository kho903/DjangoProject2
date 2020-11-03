# Instagram Clone

Cloning Instagram with Python(Django==3.1.2)

#Rquirements
- asgiref==3.2.10
- Django==3.1.2
- django-hashers-passlib==0.4
- django-rest-auth==0.9.5
- djangorestframework==3.12.1
- passlib==1.7.4
- Pillow==8.0.1
- python-mimeparse==1.6.0
- pytz==2020.1
- RestAuth==0.6.3
- RestAuthCommon==0.7.0
- six==1.15.0
- South==1.0.2
- sqlparse==0.4.1
- django-bootstrap4


## Pages:

### user
- [x] Join
- [x] Login
- [x] Logout
- [x] Delete
- [x] Change Password
- [x] User Detail
- [x] Edit Profile 
- [x] Follow 

url

http://127.0.0.1:8000/member/join/

http://127.0.0.1:8000/member/login/

http://127.0.0.1:8000/member/logout/

http://127.0.0.1:8000/member/change_password/


### photo
- [x] Create
- [x] Read - 해결
- [x] Update
- [x] Delete
- [x] DetailView
- [x] Comments - ajax 활용하여 새로고침X로 댓글 구현(코드 리팩토링 필요), 순서로직 부정확
- [x] Search - 아직 텍스트의 search만
- [x] User 
- [ ] Hashtag
- [x] Likes - comments와 같은 방법으로 구현 (코드 리팩토링 필요)

url

http://127.0.0.1:8000/photo/

http://127.0.0.1:8000/photo/<번호>

http://127.0.0.1:8000/photo/create

http://127.0.0.1:8000/photo/update/<번호>

http://127.0.0.1:8000/photo/delete/<번호>

