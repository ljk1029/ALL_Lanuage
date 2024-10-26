package GreenSdk

import (
	"encoding/json"
	"fmt"
	"github.com/gogf/gf/frame/g"
	"github.com/gogf/gf/util/gconv"
)

type AutoGenerated struct {
	Code int `json:"code"`
	Data []Data `json:"data"`
	Msg string `json:"msg"`
	RequestID string `json:"requestId"`
}
type Positions struct {
	EndPos int `json:"endPos"`
	StartPos int `json:"startPos"`
}
type Contexts struct {
	Context string `json:"context"`
	Positions []Positions `json:"positions"`
}
type Details struct {
	Contexts []Contexts `json:"contexts"`
	Label string `json:"label"`
}
type Results struct {
	Details []Details `json:"details"`
	Label string `json:"label"`
	Rate float64 `json:"rate"`
	Scene string `json:"scene"`
	Suggestion string `json:"suggestion"`
}
type Data struct {
	Code int `json:"code"`
	Content string `json:"content"`
	DataID string `json:"dataId"`
	FilteredContent string `json:"filteredContent"`
	Msg string `json:"msg"`
	Results []Results `json:"results"`
	TaskID string `json:"taskId"`
}


func WordsScan(words string,sug string) string {

	accessKeyId := g.Cfg("config").GetString("aliyunoss.AccessKeyId")
	accessKeySecret := g.Cfg("config").GetString("aliyunoss.AccessKeySecret")

	profile := Profile{AccessKeyId: accessKeyId, AccessKeySecret: accessKeySecret}

	path := "/green/text/scan"

	clientInfo := ClinetInfo{Ip: "127.0.0.1"}

	// 构造请求数据
	bizType := "default"
	scenes := []string{"antispam"}

	task := TaskWords{DataId: Rand().Hex(), Content: words}
	tasks := []TaskWords{task}

	bizData := BizDataWords{bizType, scenes, tasks}

	var client IAliYunClientWords = DefaultClient{Profile: profile}

	// your biz code
	response := client.GetResponseWord(path, clientInfo, bizData)
	fmt.Println(response)
	var revMsg AutoGenerated
	err := json.Unmarshal([]byte(response), &revMsg)
	if err != nil {
		return err.Error()
	}
	var str string
	if revMsg.Code == 200 {
		fmt.Println(revMsg)
		results := revMsg.Data[0].Results
		for _, v := range results {
			if v.Suggestion != "pass" {
				for _, value := range v.Details[0].Contexts {
					str += value.Context
				}
				if len(str) < gconv.Int(g.Cfg("config").GetString("Tips.wordsSugTip")) && len(str) > 0 {
					return sug+":"+str
				}
				return sug
			}
			fmt.Println(v.Suggestion)
		}
	}
	return ""
}
