# Instagram Clone

Cloning Instagram with Python(Django==3.1.2)

## Pages:

### user
- [x] Join
- [x] Login
- [x] Logout
- [x] Change Password
- [x] User Detail
- [x] Edit Profile : form 에 따라 약간의 DB 스키마 조정 필요, 이미지 업로드 가능하게 해야 함. 

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
- [ ] Comments - 댓글 달기 현재 ajax로 구현중 - 약간의 오류로 인해 댓글을 달고 새로고침을 누르면 추가가 됨 - 고칠예정
- [x] Search - 아직 텍스트의 search만
- [x] User 
- [ ] Hashtag
- [ ] Likes

url

http://127.0.0.1:8000/photo/

http://127.0.0.1:8000/photo/create

http://127.0.0.1:8000/photo/update/<번호>

http://127.0.0.1:8000/photo/delete/<번호>

