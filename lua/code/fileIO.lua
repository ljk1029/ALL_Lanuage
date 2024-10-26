#!/usr/local/bin/lua

function Write()
    -- 以附加的方式打开只写文件
    file = io.open("test.lua", "a")

    --检测obj是否一个可用的文件句柄
    io.type(file)

    -- 设置默认输出文件为 test.lua
    io.output(file)

    -- 在文件最后一行添加 Lua 注释
    io.write("--  test.lua 文件末尾注释")

    --向文件写入缓冲中的所有数据
    io.flush()

    -- 关闭打开的文件
    io.close(file)
end

function Read()
    -- 以只读方式打开文件
    file = io.open("test.lua", "r")

    -- 设置默认输入文件为 test.lua
    io.input(file)

    -- 输出文件第一行
    print(io.read())

    -- 关闭打开的文件
    io.close(file)
end

function FileIO()
    -- 以附加的方式打开只写文件
    file = io.open("test.lua", "a")

    --file:seek("set",2)

    -- 在文件最后一行添加 Lua 注释
    file:write("--XDF")

    -- 关闭打开的文件
    file:close()
    -- 以只读方式打开文件
    file = io.open("test.lua", "r")

    -- 输出文件第一行
    print(file:read())

    -- 关闭打开的文件
    file:close()
end


Write()
Read()
FileIO()