#!/usr/local/bin/lua

--err
function myfunction()
    n = n/nil
end
 
function myerrorhandler( err )
    print( "ERROR:", err )
end
 
status = xpcall( myfunction, myerrorhandler )
print(status)

--debug
function myfunction()
    print(debug.traceback("Stack trace"))
    print(debug.getinfo(1))
    print("Stack trace end")
        return 10
end

myfunction()
print(debug.getinfo(1))