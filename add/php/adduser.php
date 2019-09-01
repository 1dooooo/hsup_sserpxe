<?php
header("Content-type: text/html; charset=utf-8");

$phoneid = $_GET["phoneid"];
$key = $_GET["key"];

if($phoneid && $key){
    // 从文件中读取数据到PHP变量  
    $json_phoneid = file_get_contents('../../phoneid.json');  
    // 用参数true把JSON字符串强制转成PHP数组  
    $array_phoneid = json_decode($json_phoneid, true); 

    if(!in_array($phoneid, $array_phoneid["phoneid"])){
        array_push($array_phoneid["phoneid"], $phoneid);
        file_put_contents('../../phoneid.json', json_encode($array_phoneid, JSON_UNESCAPED_UNICODE));

        $config = array("key" => $key,"post_list" =>array(array("description" => "首次添加测试","id" => "75168316327377")));
        $json_config = json_encode($config, JSON_UNESCAPED_UNICODE);
        fopen('../../config/' . $phoneid . '_config.json', "w");
        file_put_contents('../../config/' . $phoneid . '_config.json', $json_config);

        $data=fopen('../../data/' . $phoneid . '_data.json', "w");
        file_put_contents('../../data/' . $phoneid . '_data.json', $json_data);
        fwrite($data,"{}");

        echo $phoneid . "的kay为: " . $key . "  添加成功";
    }else{
        echo $phoneid . "/t 已经添加过了";
    }
}else{
		echo "参数不能为空";
}

?>