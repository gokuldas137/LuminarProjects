def check_scope():
    def do_local():  #local
        test="local test"
    def non_local():
        nonlocal test
        test="non local test"
    def do_global():
        global test
        test="global test"

    test="default" #set as local inside fn...this is local
    do_local()
    print("test value after do local- "+test)  #test value is default


    non_local()   #test value is non local test
    print("test value after do non local- " + test) #non local aayondanu print ayathu


    do_global()   #ettom purathu vilikkanam...1st fn
    print("test value after do global-"+test) #ividem value of test is "NON LOCAL TEST

check_scope()

print("Global test outside functioon------"+test)  #global