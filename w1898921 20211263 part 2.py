# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20211263 
# Date: 2022-03-27


print('\nProgression Outcome Predictor')
credit = []                                                                   #creating a list
outcomes = progress = trailer = retriever = excluded = valid = 0              # declaring variables

def predictor():
    global outcomes, progress, trailer, retriever, excluded, valid            
    
    credit.clear()                                                            #clearing the list
    
    #prompting user for input and validating:
    
    while sum(credit) != 120:                                                 #total validation 
        credit.clear()                                                        #clearing the list
        valid = False
        while valid == False:
            pass_credits = input('\nPlease enter your credits at pass: ')
            validation(pass_credits)
        valid = False
        while valid == False:
            defer_credits = input('Please enter your credits at defer: ')
            validation(defer_credits)
        valid = False
        while valid == False:
            fail_credits = input('Please enter your credits at fail: ')
            validation(fail_credits)
        if sum(credit) != 120:
            print('Total Incorrect')

    #main part(the predictor):

    outcomes += 1                                                  
    if credit[0] == 120:
        print('Progress')
        progress += 1
    elif credit[0] == 100:
        print('Progress(module trailer)')
        trailer += 1
    elif credit[2] >= 80:
        print('Excluded')
        excluded += 1
    else:
        print('Do not Progress - module retriever')            
        retriever += 1
    
def validation(number):
    global valid
    try:
        number = int(number)
        valid = True
        if number in range(0,121,20):
            credit.append(number)
            valid = True
        else:
            print('Out of Range')
            valid = False
    except:
        print('Integer Required')
        
def horizontal_histogram():
    print('\n--------------------------------------------------------------')
    print('Horizontal Histogram')
    print('Progress ', progress,' : ', progress*'*')
    print('Trailer ', trailer,'  : ', trailer*'*')
    print('Retriever ', retriever,': ', retriever*'*')
    print('Excluded ', excluded,' : ', excluded*'*','\n')
    print(outcomes,'outcome(s) in total')
    print('--------------------------------------------------------------\n')

def vertical_histogram(outcomes,progress,trailer,retriever,excluded):
    print('--------------------------------------------------------------')
    print('Vertical Histogram')
    print('Progress','\tTrailer','\tRetriever','\tExcluded')
    while(progress != 0 or trailer != 0 or retriever != 0 or excluded != 0):
        if progress != 0:
            print('*',end='')
            progress -= 1
        else:
            print('',end='')
        if trailer != 0:
            print('\t\t*',end='')
            trailer -= 1
        else:
            print('\t\t',end='')
        if retriever != 0:
            print('\t\t*',end='')
            retriever -= 1
        else:
            print('\t\t',end='')
        if excluded != 0:
            print('\t\t*')
            excluded -= 1
        else:
            print('\t\t')
    print('\n'+str(outcomes),'outcome(s) in total')
    print('--------------------------------------------------------------\n')
        
def menu():
    option = input('''\nEnter a suitable option out of the following:
    \n1 - Student Version\n2 -  Staff Version\n3 - Quit\n\nOption: ''')
    if option == '1':
        print('\nStudent Version')
        predictor()
        menu()        
    elif option == '2':
        print('\nStaff Version with Histograms')
        predictor()
        status = 0
        while status != 'q':
            status = input('\nWould you like to enter another set of data?\nEnter \'q\' to quit and view results OR anything else to proceed: ')
            if status != 'q':
                predictor()
        horizontal_histogram()                                              #only the staff version facilitates printing histograms
        vertical_histogram(outcomes,progress,trailer,retriever,excluded)
    elif option == '3':
        return        
    else:
        print('\nPlease enter a valid option')
        menu()
        
menu()
