<?php 
header("Content-type: text/html; charset=utf-8");

$phoneid = $_GET["phoneid"];
$name = $_GET["name"];
$id = $_GET["id"];

if( $phoneid && $name && $id ){

    // 从文件中读取数据到PHP变量  
    $json_phoneid = file_get_contents('../../phoneid.json');  
    // 用参数true把JSON字符串强制转成PHP数组  
    $array_phoneid = json_decode($json_phoneid, true); 

    if(!in_array($phoneid, $array_phoneid["phoneid"])){
        echo $phoneid . "用户未添加kay, 访问/adduser.html 进行添加";
    }else{
        $json_config = file_get_contents('../../config/' . $phoneid . '_config.json');
        $config = json_decode($json_config, true); 

        $item_flag = FALSE;
        foreach($config["post_list"] as $item){
            if($item["id"] == $id){
                $item_flag = TRUE;
                break;
            }
        }
        if(!$item_flag){
            array_push($config["post_list"], array('description'=>$name, 'id'=>$id));

            $json_string = json_encode($config, JSON_UNESCAPED_UNICODE);
            file_put_contents('../../config/' . $phoneid . '_config.json', $json_string);


            echo $name . "的运单号为:" . $id . "添加成功<br><br><br>";
            echo "目前存在的快递有:<br>";
            foreach($config["post_list"] as $item){
                echo "<br>名字：" . $item["description"] . "---运单号：" . $item["id"];
            }
        }else{
            echo "运单号:" . $id . "已经存在了";
        }

    }
}else{
  echo "参数不允许为空";
}
?>