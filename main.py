from key import App_access_token        #importing App_access_token from another file
import requests     #importing request library
import urllib       #importing urllib library
Base_url = "https://api.instagram.com/v1/"


#defining a function to fetch self information
def self_info():
    request_url = Base_url + "users/self/?access_token=%s" %(App_access_token)
    user_info = requests.get(request_url)
    user_info = user_info.json()


    if user_info['meta']['code'] == 200:        #200 means ecerything is going well
        if len(user_info['data']):
            print "User name: %s" % (user_info['data']['username'])
            print "Followers:  %s" % (user_info['data']['counts']['followed_by'])
            print "Following:  %s" % (user_info['data']['counts']['follows'])
            print "Posts:  %s" % (user_info['data']['counts']['media'])
        else:
            print "User does not exist!!"
    else:
        print "code other than 200!!!"



#defining function to know the user id by his/her username
def get_user_id(insta_user_name):
    request_url = Base_url + "users/search?q=%s&access_token=%s" %(insta_user_name,App_access_token)
    user_info = requests.get(request_url)
    user_info = user_info.json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print "code other than 200!!"



#defining function to get user information
def get_user_info(insta_user_name):
    user_id = get_user_id(insta_user_name)      #calls get_user_id function to get the user id
    if user_id == None:
        print "User doesnot exist!!"
    request_url = Base_url + "users/%s/?access_token=%s" % (user_id,App_access_token)
    user_info = requests.get(request_url)
    user_info = user_info.json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print "User name: %s" %(user_info['data']['username'])
            print "Number of followers: %s" %(user_info['data']['counts']['followed_by'])
            print "Number of users you are following: %s" %(user_info['data']['counts']['follows'])
            print "Number of posts: %s" %(user_info['data']['counts']['media'])
        else:
            print "No data for this user exist!!"
    else:
        print "Code other than 200"


#defining function to fetch recent post of owner of access token
def get_own_post():
    request_url = Base_url +"users/self/media/recent/?access_token=%s" %(App_access_token)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] +".jpeg"
            image_url =  own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print "Your image has been downloaded!!"
        else:
            print "Media does not exist!!"
    else:
        print "Code other than 200!!"


#defining a function to get the id of recent media
def get_media_id(insta_user_name):
    user_id = get_user_id(insta_user_name)
    if user_id == None:
        print "User does not exist!!"
    request_url = Base_url + "users/%s/media/recent/?access_token=%s" % (user_id, App_access_token)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            media_id = user_media['data'][0]['id']
            return media_id
        else:
            print "Media does not exist!!"
    else:
        print "Code other than 200!!"


#defining a function to get a list of comments in recent post
def get_comment_list(insta_user_name):
    media_id = get_media_id(insta_user_name)
    request_url = Base_url + "media/%s/comments?access_token=%s" %(media_id, App_access_token)
    user_comments = requests.get(request_url).json()
    if user_comments['meta']['data'] == 200:
        if user_comments['data']:
            print "Comment at: %s" %(user_comments['data']['created_time'])
            print "Comment is: %s" %(user_comments['data']['text'])
            print "Comment from: %s" %(user_comments['data']['from']['username'])

        else:
            print "Media does not exist!!"
    else:
        print "Code other than 200!!"








#defining function to get the recent post of user by his/her name
def get_user_post(insta_user_name):
    user_id = get_user_id(insta_user_name)
    if user_id == None:
        print "User does not exist!!"
    request_url = Base_url + "users/%s/media/recent/?access_token=%s" %(user_id, App_access_token)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] +".jpeg"
            image_url =  user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print "Your image has been downloaded!!"
        else:
            print "Media does not exist!!"
    else:
        print "Code other than 200!!"




#defining function to like a post of the user by his/her username
def like_post():
    media_id = get_media_id(insta_user_name)
    request_url = Base_url + "media/%s/likes" %(media_id)
    payload = { "access_token" : App_access_token}
    like_media = requests.post(request_url,payload).json()
    if like_media['meta']['code'] == 200:
        print "You liked the post"
    else:
        print "Your like was unsuccessful! Try again!!"



#defining function to post a comment on recent post of user
def post_comment():
    media_id = get_media_id(insta_user_name)
    comment = raw_input("What do you want to comment?")
    request_url = Base_url +"media/%s/comments" %(media_id)
    payload = { "access_token" : App_access_token, "text" : comment}
    comment_info = requests.post(request_url, payload).json()
    if comment_info['meta']['code'] == 200:
        print "Comment posted successfully!!"
    else:
        print "Comment posting not successfull. Try again!!"





#defining our main function calling other functions
def start_bot():
    while True:
        print "Welcome to InstaBot"
        print "Here is the menu, Select the option according to your requirements!!"
        print "a.Get your own details"
        print "b.Get details of any user by his/her username"
        print "c.Get own recent post"
        print "d.Get recent post of user by his/her name"
        print "e.Get comment list of a media"
        print "f.Like a recent post of the user by his/her username"
        print "g.Exit "

        choice = raw_input("What you want to do?")
        if choice == "a":       #to get detials of the owner of the access token
            self_info()
        elif choice == "b":     #to get detials of a user
            insta_user_name = raw_input("Enter the user name whose information you want to fetch: ")
            get_user_info(insta_user_name)
        elif choice == "c":     #to get own recent post
            get_own_post()
        elif choice == "d":     #to get recent post of user
            insta_user_name = raw_input("Enter the name of the user whose recent post you want to fetch?")
            get_user_post(insta_user_name)
        elif choice == "e":     #to get comment list of recent post of user
            insta_user_name = raw_input("Enter the name of the user whose comment list you want to fetch?")
            get_comment_list(insta_user_name)
        elif choice == "f":     #to like recent post of user
            insta_user_name = raw_input("Enter the name of the user whose recent post you want to like?")
            like_post(insta_user_name)
        elif choice == "g":     #to exit
            exit()
        else:
            print "Enter alphbet from a to c only"


start_bot()