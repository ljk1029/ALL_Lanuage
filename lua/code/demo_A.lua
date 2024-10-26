#!/usr/local/bin/lua

--[[
多行注释
基础功能学习
local 为局部变量
其他默认为全局变量
--]]

--打印
function Print()
    --字符串
    print("Hello World！")
    print('www.runoob.com')
    print(1,2e-2,2e+3)

    --数据类型
    print(type("Hello world")) 
    print(type(10.4*3)) 
    print(type(print)) 
    print(type(type))
    print(type(true)) 
    print(type(nil)) 
    print(type(type(X)))

    --运算符
    -- ..连接
    print("连接字符串 a 和 b ", "Hello ".."World" )
    -- #长度
    print("b 字符串长度 ",#"World" )
end

--table使用
function Table()
    tab1 = { key1 = "val1", key2 = "val2", "val3" }
    for k, v in pairs(tab1) do
        print(k .. " - " .. v)
    end

    --table, 赋值nil等于删除
    tab1.key1 = nil
    for k, v in pairs(tab1) do
        print(k .. " - " .. v)
    end

    -- 创建一个数组
    local myArray = {10, 20, 30, 40, 50}

    -- 循环遍历数组
    for i = 1, #myArray do
        print(myArray[i])
    end
end

--字符串使用
function String()
    --nil作为比较应加上""
    -- 定义一个变量X，但未为其赋值
    x='nil'  -- 全局变量
    local X  -- 局部变量
    
    -- 检查X的类型
    if type(X) == "nil" then
        print("X is nil")
    else
        print("X is not nil")
    end

    --也可以用 2 个方括号 "[[]]" 来表示"一块"字符串。
    html = [[
        <html>
        <head></head>
        <body>
            <a href="http://www.runoob.com/">菜鸟教程</a>
        </body>
        </html>
    ]]
    print(html)

    --字符串长度
    print("html len:", string.len(html))
    print("html len:", utf8.len(html))
end

--固定参数
function Factorial(n)
    print(n)
    if n == 0 then
        return 1
    else
        return n * Factorial(n - 1)
    end
end

--可变参数
function Add(...) 
    local s = 0  
    local c = 0  
    for i, v in ipairs{...} do
        s = s + v
        c = i  
    end  
    return s, c
end  

--赋值
function Operation()
    --赋值
    a,b,c = 3, 7
    print(a,b,c)

    --交换
    a,b = b,a
    print(a,b,c)

    --整除
    c = a//b
    --返回多个参数

    d = a~=b
    return a, b, c, d
end

--循环
function Loop()
    --while
    cnt = 0
    while( cnt < 5 )
    do
        cnt = cnt+1
        print("while 次数",cnt)
    end
end



--[[
    中阶功能学习
--]]

--线程
function Thread()
    --print(2)
end

--自定义
--function Userdata
    --print(1)
--end




--[[
    高阶功能学习
--]]
--#LUA_PATH 需要导入环境变量例如~/lua/   将?改为你模块名
--export LUA_PATH="~/lua/?.lua;;"
--export LUA_PATH="/mnt/hgfs/MyWork/C_LUA/luaCode/module.lua;;"
-- 定义一个名为 module 的模块
function Module()
    --require("<模块名>")
    require "<module>"
    print(module.constant)
    module.func3()
end

-- 打包
function Pack()
    local path = "/usr/local/lua/lib/libluasocket.so"
    local f = assert(loadlib(path, "luaopen_socket"))
    f()  -- 真正打开库
end



--main
function main()
    Print()
    Table()
    String()

    --函数也可以赋值
    print("Factorial 5:",  Factorial(5))
    factorial2 = Factorial
    print("Factorial2 5:", factorial2(5))
    print("Add 2 3 4:",    Add(2,3,4))
    print("Operation return:", Operation())
    Loop()

    Module()
end

main()