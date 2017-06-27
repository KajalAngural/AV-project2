from key import App_access_token        #importing App_access_token from another file
import requests     #importing request library
Base_url = "https://api.instagram.com/v1/"


#defining a function to fetch self information
def self_info():
    request_url = Base_url + "users/self/?access_token=%s" %(App_access_token)
    print "GET request url = %s" %(request_url)
    user_info = requests.get(request_url)
    user_info = user_info.json()


    if user_info['meta']['code'] == 200:        #200 means ecerything is going well
        if len(user_info['data']):
            print "User name: %s" %(user_info['data']['username'])
            print "Followers:  %s" %(user_info['data']['counts']['followed_by'])
            print "Following:  %s" % (user_info['data']['counts']['follows'])
            print "Posts:  %s" % (user_info['data']['counts']['media'])
        else:
            print "User does not exist!!"
    else:
        print "code other than 200!!!"



#defining function to know the user id by his/her username
def get_user_id(insta_user_name):
    request_url = Base_url + "users/search?q=%s&access_token=%s" %(insta_user_name,App_access_token)
    print "GET request url = %s" %(request_url)
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
    print "GET request url = %s" %(request_url)
    user_info = requests.get(request_url)
    user_info = user_info.json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print "User name: %s" %(user_info['data']['username'])
            print "Number of followers: %s" (user_info['data']['counts']['followed_by'])
            print "Number of users you are following: %s"(user_info['data']['counts']['follows'])
            print "Number of posts: %s"(user_info['data']['counts']['media'])
        else:
            print "No data for this user exist!!"
    else:
        print "Code other than 200"




#defining our main function calling other functions
def start_bot():
    while True:
        print "Welcome to InstaBot"
        print "Here is the menu, Select the option according to your requirements!!"
        print "a.Get your own details\nb.Get details of nay user by his/her username\nc.Exit "

        choice = raw_input("What you want to do?")
        if choice == "a":
            self_info()
        elif choice == "b":
            insta_user_name = raw_input("Enter the user name whose information you want to fetch: ")
            get_user_info(insta_user_name)
        elif choice == "c":
            exit()
        else:
            print "Enter alphbet from a to c only"


start_bot()