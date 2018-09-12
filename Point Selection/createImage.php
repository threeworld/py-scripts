<?php
/**
 * 中文点选验证码生成
 */
ob_end_clean();
header( "Content-Type:text/html; charset=UTF-8 ");
function createImage($word,$imagePath,$type,$imageName){
    $fontPath = 'C:\Windows\Fonts\Arvo-Regular.ttf';//字体
    switch ($type) {
        case 0://mp 文字随机大小
            $fontSize = rand(20,30) * 0.75;
            break;
         case 1://ap 文字固定
            $fontSize = 20 * 0.75;
            break; 
    }
    foreach ($word as $v ) {
        $fontarea  = imagettfbbox($fontSize, 0, $fontPath, $v);
        $textWidth = $fontarea[2] - $fontarea[0];
        $textHeight = $fontarea[1] - $fontarea[7];
        $tmp['text'] = $v;
        $tmp['size'] = $fontSize;
        $tmp['width'] = $textWidth;
        $tmp['height'] = $textHeight;
        $textArr[] = $tmp;
    }
    list($imageWidth, $imageHeight, $imageType) = getimagesize($imagePath);
    for($i=0;$i<count($textArr);$i++){
        list($x, $y) = randPosition($textArr, $imageWidth, $imageHeight, $textArr[$i]['width'], $textArr[$i]['height'],$i,$type);
        $textArr[$i]['x'] = $x;
        $textArr[$i]['y'] = $y;
    }
    unset($v);
    
    //创建图片的实例
    $image = imagecreatefromstring(file_get_contents($imagePath));
    //字体颜色
    $color = imagecolorallocate($image, 0, 0, 0);
    //绘画文字
    foreach($textArr as $v){
        imagefttext($image, $v['size'], 0, $v['x'], $v['y'], $color, $fontPath, $v['text']);
    }
    if(imagepng($image,$imageName)){
        echo $imageName."\n";
    }
}
function randPosition($textArr, $imgW, $imgH, $fontW, $fontH,$i,$type){
	switch ($type) {
		case 0://生成mp
			$x = rand($i*60, ($i+1)*60-$fontW-3);
			$y = rand(40,80); 
			break;
		case 1://生成ap
			$x = ($i)*25+5;
			$y = 25;
		default:
			break;
	}
    $return = array($x, $y);
    return $return;
}
$ap_imagePath = 'ap_bg.png';
$mp_imagePath = 'mp_bg.png';
$ap_imageName = "ap_".time().".png";
$mp_imageName = "mp_".time().".png";
$ap_word = array('p','l','e','a','s','e','a','n','d', 's','c') ;
$mp_word = array('a', 'n', 'd','s','c');
createImage($ap_word,$ap_imagePath,1,$ap_imageName);
createImage($mp_word,$mp_imagePath,0,$mp_imageName);
?>