import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import numpy as np
import difflib
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity,linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import bs4
from bs4 import BeautifulSoup
import requests
from urllib.request import*
import webbrowser
import mysql.connector
import streamlit.components.v1 as components
mydb = mysql.connector.connect(
host="localhost",
user="root",
port=3306,
password="",
database="datas"
)
mycursor = mydb.cursor()
def add_user(username,mail,password):
  sql = "INSERT INTO register(username,mail,password) VALUES (%s, %s, %s)"
  val = (username,mail,password)
  mycursor.execute(sql,val)
  mydb.commit()
  st.success("Registered successfulLy")
def login_user(username2,mail10,password1):
	sql = """SELECT * FROM register WHERE username=%s AND mail=%s AND password=%s """
	result=mycursor.execute(sql,(username2,mail10,password1))
	if(result!=0):
		data=mycursor.fetchall()
		if(data!=[]):
			st.success("login successful")
			st.session_state['flag']=1
		else:
		    st.error("incorrect password or username")


st.title("BOOK RECOMMENDATION SYSTEM")
with open('style.css') as f:
	st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
st.markdown("""
<style>
.css-9s5bis.edgvbvh3{
visibility:hidden
}
</style>
""",unsafe_allow_html=True)

st.markdown("""
<style>
.css-h5rgawegzxvld1{
visibility:hidden
}

</style>
""",unsafe_allow_html=True)
def main():
	def add_bg_from_url():
		st.markdown(
		f"""
		<style>
		.stApp {{

		background-image: url("https://t4.ftcdn.net/jpg/05/20/52/45/360_F_520524506_uzUOhx0eU3w7gBggVZezwDyPzexTtr9Q.jpg");
		background-attachment: fixed;
		background-size: cover
		}}
		image {{
		height:10px;
		}}
		write{{
		font-size:200px;

		}}
		</style>
		""",
		unsafe_allow_html=True )

	l=[]
	def load_data(data):
		df=pd.read_csv(data)
		return df
	add_bg_from_url()
	image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjwR_qwwP-PgM2uGa5crh8YvIhpV_yc7LNXA&usqp=CAU"
	st.sidebar.image(image)
	
	menu=["HOME","ABOUT","RECOMMEND BASED ON BOOK","RECOMMEND BASED ON AUTHOR","BEST BOOKS","REGISTER","LOGIN","PROFILE"]
	choice=st.sidebar.selectbox("Menu",menu)
	st.sidebar.header("TRENDING BOOKS")
	st.sidebar.info("")
	if choice=="HOME":
		st.header("CATEGORIES")
		html=urlopen("https://www.panmacmillan.com/blogs/general/must-read-books-of-all-time").read()
		soup=BeautifulSoup(html)
		title=soup.find_all('li',class_='block float-left mb-2 mr-2')
		col1,col2=st.columns(2)
		subm2=col1.button('Literary fiction books')
		subm1=col1.button('Classic books')
		subm3=col1.button('Sci-fi and fantasy books')
		subm4=col1.button('Non-fiction books')
		subm5=col1.button('Crime and thriller books')
		subm6=col1.button('Historical fiction books')
		subm7=col1.button('Books in translation')
		subm8=col1.button('Dystopian books')
		if(subm2):
			df=load_data('books.csv')
			book=df['Books']
			for i in range(8):
				with st.container():
					if(i%2==0):
						col2.subheader(book[i])
					else:
						col2.subheader(book[i])
		elif(subm1):
			df=load_data('books.csv')
			book=df['Books']
			for i in range(8):
				with st.container():
					if(i%2==0):
						col2.subheader(book[i+8])
					else:
						col2.subheader(book[i+8])
		elif(subm3):
			df=load_data('books.csv')
			book=df['Books']
			for i in range(8):
				with st.container():
					if(i%2==0):
						col2.subheader(book[i+8+7])
					else:
						col2.subheader(book[i+8+7])  			
		elif(subm4):
			df=load_data('books.csv')
			book=df['Books']
			for i in range(7):
				with st.container():
					if(i%2==0):
						col2.subheader(book[i+8+15])
					else:
						col2.subheader(book[i+8+15]) 
		elif(subm5):
			df=load_data('books.csv')
			book=df['Books']
			for i in range(6):
				with st.container():
					if(i%2==0):
						col2.subheader(book[i+8+22])
					else:
						col2.subheader(book[i+8+22]) 
		elif(subm6):
			df=load_data('books.csv')
			book=df['Books']
			for i in range(5):
				with st.container():
					if(i%2==0):
						col2.subheader(book[i+8+22+6])
					else:
						col2.subheader(book[i+8+22+6]) 
		elif(subm7):
			df=load_data('books.csv')
			book=df['Books']
			for i in range(4):
				with st.container():
					if(i%2==0):
						col2.subheader(book[i+8+22+11])
					else:
						col2.subheader(book[i+8+22+11]) 
		elif(subm8):
			df=load_data('books.csv')
			book=df['Books']
			for i in range(4):
				with st.container():
					if(i%2==0):
						col2.subheader(book[i+8+22+11+4])
					else:
						col2.subheader(book[i+8+22+11+4]) 
	elif choice=="BEST BOOKS":
		df=load_data('books.csv')
		x=0
		for i in df:
			col1,col2=st.columns(2)
			if(x<11):
				with st.container():
					st.info("")
					col1.subheader(df['Books'][x])
					col1.subheader(df['Authors'][x])
					col2.image(df['images'][x],width=200)
					link='[BUY NOW]({link})'.format(link=df['link'][x])
					col1.markdown(link,unsafe_allow_html=True)
					x=x+1
	elif choice=="RECOMMEND BASED ON BOOK":
		st.subheader("Recommend books")
		search_term=st.text_input("Search here")
		if st.button("RECOMMEND"):
			flag = st.session_state.get('flag', None)
			if(flag==None):
				st.error("Login to search")
			elif search_term is not None:
				try:
					df=load_data('books.csv')
					st.session_state['search_term']=search_term
					book_selected=['Books']
					for i in book_selected:
						df[i]=df[i].fillna('')
						book_combined=df['Books']
						vectorizer=TfidfVectorizer()
						feature_vector=vectorizer.fit_transform(book_combined.values.astype('U'))
						similarity=cosine_similarity(feature_vector)
						list_books=df['Books'].tolist()
						close_match=difflib.get_close_matches(search_term,list_books)
						n=0
						f=0
						index=0
						for i in list_books:
							n=n+1
							if(i==close_match[0]):
								index=n-1
								break
						similarity=list(enumerate(similarity[index]))
						sorted_similarity=sorted(similarity,key=lambda x:x[1],reverse=True)
						st.subheader("Boooks suggested for you:")
						x=1
						for i in sorted_similarity:
							index=i[0]
							t=df[df.index==index]['Books'].values[0]
							a=df[df.index==index]['Authors'].values[0]
							b=df[df.index==index]['images'].values[0]
							l=df[df.index==index]['link'].values[0]
							col1,col2=st.columns(2)
							if(x<11):
								with st.container():
									st.info("")
									col1.subheader(x)
									col1.subheader(t)
									col1.subheader(a)
									col2.image(b,width=200)
									link='[BUY NOW]({link})'.format(link=l)
									col1.markdown(link,unsafe_allow_html=True)
									x=x+1
				except Exception as e:
					raise e
					result="not found"
					st.write(result)
	elif choice=="PROFILE":
		n= st.session_state.get('username')
		m= st.session_state.get('mail')
		p= st.session_state.get('password')
		a=st.session_state.get('search_term')
		img="https://previews.123rf.com/images/sarahdesign/sarahdesign1506/sarahdesign150605280/41564095-my-account-icon.jpg"

		st.image(img,channels="BGR",width=200)
		l.append(a)
		st.write("NAME: ",n)
		st.write("MAIL: ",m)
		st.write("PASSWORD: ",p)
		for i in l:
			st.write("PREVIOUSLY SEARCHED: ",i)
	elif choice=='ABOUT':
		new_title = '<p style="font-family:sans-serif; color:white; font-size: 42px;">ABOUT</p>'
		st.markdown(new_title, unsafe_allow_html=True)
		image="https://ik.imagekit.io/panmac/tr:f-auto,w-740,pr-true//bcd02f72-b50c-0179-8b4b-5e44f5340bd4/fc0a6bb9-f67f-4b66-902e-462e02cbb662/Must-reads-50-best-books-of-all-time.jpg"
		st.image(image, channels="BGR",width=400)
		text='<p style="font-size:20px;position:relative;">In higher education a course is a unit of teaching that typically lasts one academic term, is led by one or more instructors, and has a fixed roster of students. A course usually covers an individual subject. Courses generally have a fixed program of sessions every week during the term, called lessons or classes.")</p>'
		st.markdown(text, unsafe_allow_html=True)
	elif choice=="REGISTER":
		st.subheader("CREATE NEW ACCOUNT")
		with st.form(key='form2'):
			mail=st.text_input("MAIL")
			username=st.text_input("USER NAME")
			password=st.text_input("PASSWORD",type="password")
			subm=st.form_submit_button(label="REGISTER")
		if subm==True:
			add_user(username,mail,password)
	elif choice=="RECOMMEND BASED ON AUTHOR":
		st.subheader("Recommend books")
		search_term=st.text_input("Search here")
		if st.button("RECOMMEND"):
			flag = st.session_state.get('flag', None)
			if(flag==None):
				st.error("Login to search")
			elif search_term is not None:
				try:
					df=load_data('books.csv')
					st.session_state['search_term']=search_term
					book_selected=['Authors']
					for i in book_selected:
						df[i]=df[i].fillna('')
						book_combined=df['Authors']
						vectorizer=TfidfVectorizer()
						feature_vector=vectorizer.fit_transform(book_combined.values.astype('U'))
						similarity=cosine_similarity(feature_vector)
						list_books=df['Authors'].tolist()
						close_match=difflib.get_close_matches(search_term,list_books)
						n=0
						f=0
						index=0
						for i in list_books:
							n=n+1
							if(i==close_match[0]):
								index=n-1
								break
						similarity=list(enumerate(similarity[index]))
						sorted_similarity=sorted(similarity,key=lambda x:x[1],reverse=True)
						st.subheader("Boook suggested for you:")
						x=1
						for i in sorted_similarity:
							index=i[0]
							t=df[df.index==index]['Books'].values[0]
							a=df[df.index==index]['Authors'].values[0]
							b=df[df.index==index]['images'].values[0]
							l=df[df.index==index]['link'].values[0]
							col1,col2=st.columns(2)
							if(x<2):
								with st.container():
									st.info("")
									col1.subheader(x)
									col1.subheader(t)
									col1.subheader(a)
									col2.image(b,width=200)
									col1.subheader("Click here:[Know here](https://archive.nptel.ac.in/noc/courses/noc22/SEM1/noc22-ph08/)")
									link='[BUY NOW]({link})'.format(link=l)
									col1.markdown(link,unsafe_allow_html=True)
									x=x+1
				except Exception as e:
						raise e
						result="not found"
						st.write(result)
	elif choice=="LOGIN":
		st.subheader("LOGIN SECTION")
		with st.form(key='form1'):
			mail10=st.text_input("EMAIL")
			username2=st.text_input("NAME")
			password1=st.text_input("PASSWORD",type="password")
			st.session_state['username']=username2
			st.session_state['mail']=mail10
			st.session_state['password']=password1
			submit=st.form_submit_button("LOGIN")
		if submit:
		    login_user(username2,mail10,password1)
    
	
    
    
if __name__=='__main__':
   main()