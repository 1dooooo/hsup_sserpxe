<?php 
header("Content-type: text/html; charset=utf-8");

$phoneid = $_GET["phoneid"];
$name = $_GET["name"];
$id = $_GET["id"];

if( $phoneid && $name && $id ){

    if(!file_exists('../../phoneid.json')){
        echo "请先添加用户";
        die();
    }else{
        // 从文件中读取数据到PHP变量  
        $json_phoneid = file_get_contents('../../phoneid.json');  
        // 用参数true把JSON字符串强制转成PHP数组  
        $array_phoneid = json_decode($json_phoneid, true);
    }

    if(!in_array($phoneid, $array_phoneid["phoneid"])){
        echo $phoneid . "用户未添加kay, 访问/adduser.html 进行添加";
    }else{
        $json_config = file_get_contents('../../config/' . $phoneid . '_config.json');
        $config = json_decode($json_config, true); 

        if(!$config["items"][$id]){
            $config["items"][$id] = array('description'=>$name, 'company'=>"");

            $json_string = json_encode($config, JSON_UNESCAPED_UNICODE);
            file_put_contents('../../config/' . $phoneid . '_config.json', $json_string);


            echo $name . "的运单号为:" . $id . "添加成功<br><br><br>";
            echo "目前存在的快递有:<br>";
            foreach($config["items"] as $k => $v){
                echo "<br>名字：" . $v["description"] . "---运单号：" . $k;
            }
        }else{
            echo "运单号:" . $id . "已经存在了";
        }

    }
}else{
  echo "参数不允许为空";
}
?>