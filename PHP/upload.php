<?php

if(isset($_FILES['file'])){
    $file = $_FILES['file'];
    
    // File properties
    $file_name = $file['name'];
    $file_tmp = $file['tmp_name'];
    $file_size = $file['size'];
    $file_error = $file['error'];
    
    // Work out the file extension
    $file_ext = explode('.',$file_name);
    $file_ext = strtolower(end($file_ext));
    
    $allowed = array('txt', 'pdf', 'csv', 'jpg', 'jpeg');
    
    if(in_array($file_ext, $allowed)){
        if($file_error === 0){
            if($file_size <= 5000000){
                $uniq_id = uniqid('', true);
                $file_name_new =  $uniq_id.'.'.$file_ext;
                $file_destination = 'Uploads/' . $file_name_new;
                
                echo 'File has been uploaded sucessfully<br>';
                
                $status_url = './status?id='.$uniq_id;
                echo "Status can be checked <a href='$status_url'>Here</a>";
                
                if(move_uploaded_file($file_tmp, $file_destination)){
                    $file_destination;
                }
                file_get_contents('http://localhost:8080/process-file?id='.$uniq_id);
            }
        }
    }  
}

