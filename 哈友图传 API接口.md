哈友图传 API 接口说明文档

1.  API 类型：

    /osc/info 获取 接口信息

    /osc/state

    /osc/checkForUpdates 检查更新

    /osc/commands/execute 执行API命令 (可用）

    /osc/commands/status ，API命令状态

2.  API 接口

-   uart.send (可用）

    发送数据到 串口 TXD 引脚：

    示例：

    url：<http://192.168.0.1/osc/commands/execute>

    GET方式，Body 内容：

    {\"name\":\"uart.send\",\"data\":\"test12312343\"}

    ![](media/image1.png){width="5.761805555555555in"
    height="3.2354166666666666in"}

    波特率 115200 ，请使用 json 编码后发送
    ，请勿携带任何换行字符。否则可能会执行错误指令。

    ![](media/image2.png){width="5.759722222222222in"
    height="3.2402777777777776in"}

    中文字符需要进行unicode编码才能传输，不建议传输使用json
    编码传输二进制数据，应当再base64编码后，再通过json封装。

-   uart.rcv (可用）

    从 串口 RXD 引脚 ，波特率 115200 接受数据：

    串口发送数据后，加入两个换行符。禁止使用非编码字符。二进制数据建议使用
    base64编码后发送。

    网络端，使用 uart.rcv 接口接收数据。

    示例：

    url：<http://192.168.0.1/osc/commands/execute>

    GET方式，Body 内容：

    {\"name\":\"uart.rcv\"}

    ![](media/image3.png){width="5.759722222222222in"
    height="3.2402777777777776in"}

```{=html}
<!-- -->
```
-   camera.listFile ：列出文件 (暂时不可用）

    API示例：

    url：<http://192.168.0.1/osc/commands/execute>

    GET方式，Body 内容：

    {\"name\":\"camera.listFile\",\"parameters\":{\"fileType\":\"video\",\"entryCount\":1,\"maxThumbSize\":1000000000}}

3.  API接口示例：

    通过TCP 发送如下内容 到 80端口：

    GET /osc/commands/execute HTTP/1.1

    Host: 192.168.0.1

    Connection: keep-alive

    {\"name\":\"camera.takePicture\"}

    注意，最后内容带两个换行符。

    ![](media/image4.png){width="5.764583333333333in"
    height="5.206944444444445in"}

    返回：

    拍照命令 (暂时不可用）

HTTP/1.1 200 OK

Expires: 0

Max-Age: 0

Content-Type: application/json; charset=utf-8

Content-Length: 89

X-Content-Type-Options: nosniff

Connection: close

{\"name\":\"camera.takePicture\",\"state\":\"inProgress\",\"id\":\"2\",\"progress\":{\"completion\":0.0}}

查询API 命令状态：

GET /osc/commands/status HTTP/1.1

Host: 192.168.0.1

Connection: keep-alive

{\"name\":\"camera.takePicture\"}

返回：

HTTP/1.1 400 Bad Request

Expires: 0

Max-Age: 0

Content-Type: application/json; charset=utf-8

Content-Length: 118

X-Content-Type-Options: nosniff

Connection: close

{\"name\":\"camera.startSession\",\"state\":\"error\",\"error\":{\"code\":\"missingParameter\",\"message\":\"parameter
id is missing\"}}

4.  返回数据示例：

    /osc/info

> HTTP/1.1 200 OK
>
> Expires: 0
>
> Max-Age: 0
>
> Content-Type: application/json; charset=utf-8
>
> Content-Length: 354
>
> X-Content-Type-Options: nosniff
>
> Connection: close

{\
    **\"manufacturer\"**:**\"RICOH\"**,\
    **\"model\"**:**\"RICOH THETA S\"**,\
    **\"serialNumber\"**:**\"01106502\"**,\
    **\"firmwareVersion\"**:**\"01.82\"**,\
    **\"supportUrl\"**:**\"https://theta360.com/en/support/\"**,\
    **\"endpoints\"**:{\
        **\"httpPort\"**:**80**,\
        **\"httpUpdatesPort\"**:**80**\
    },\
    **\"gps\"**:**false**,\
    **\"gyro\"**:**false**,\
    **\"uptime\"**:**60**,\
    **\"api\"**:\[\
        **\"/osc/info\"**,\
        **\"/osc/state\"**,\
        **\"/osc/checkForUpdates\"**,\
        **\"/osc/commands/execute\"**,\
        **\"/osc/commands/status\"**\
    \],\
    **\"apiLevel\"**:\[\
        **1**,\
        **2**\
    \]\
}
