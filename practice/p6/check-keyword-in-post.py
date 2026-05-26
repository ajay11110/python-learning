post = input("enter your post content here L:")
keyWord = input("enter your key word to find in the post :")

if(keyWord.lower() in post.lower()) :
    print("Yes, this keyword is available in post")

else:
        print("No, this keyword is not available in post")