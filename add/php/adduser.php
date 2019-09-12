<?php
header("Content-type: text/html; charset=utf-8");

$phoneid = $_GET["phoneid"];
$key = $_GET["key"];

if($phoneid && $key){
    if (file_exists('../../phoneid.json')){
        // 从文件中读取数据到PHP变量  
        $json_phoneid = file_get_contents('../../phoneid.json');

        // 用参数true把JSON字符串强制转成PHP数组 
        $array_phoneid = json_decode($json_phoneid, true);
        if(!in_array($phoneid, $array_phoneid["phoneid"])){
            array_push($array_phoneid["phoneid"], $phoneid);

        }else{
            echo $phoneid . " 已经添加过了";
            die();
        }
    }else{
        //首次使用创建  初始化文件环境
        fopen('../../phoneid.json', "w");

        $array_phoneid = array("phoneid" => array($phoneid));
    }
    file_put_contents('../../phoneid.json', json_encode($array_phoneid, JSON_UNESCAPED_UNICODE));
    
    //为新用户创建 config 文件, 并加入测试数据
    if(!is_dir('../../config')){
        mkdir('../../config');
    }
    $config = array("key" => $key,"items" =>array("75168316327377" => array("description" => "首次添加测试","company" => "yto")));
    $json_config = json_encode($config, JSON_UNESCAPED_UNICODE);
    fopen('../../config/' . $phoneid . '_config.json', "w");
    file_put_contents('../../config/' . $phoneid . '_config.json', $json_config);

    //为新用户创建 data 文件
    if(!is_dir('../../data')){
        mkdir('../../data');;
    }
    $data=fopen('../../data/' . $phoneid . '_data.json', "w");
    fwrite($data,"{}");

    echo $phoneid . "的kay为: " . $key . "  添加成功";
    
}else{
	echo "参数不能为空";
}

?>