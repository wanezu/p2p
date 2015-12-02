function loadArea(areaId,areaType) {
    $.post(ajaxurl,{'areaId':areaId},function(data){
        if(areaType=='city'){
           $('#'+areaType).html('<option value="-1">市/县</option>');
           $('#district').html('<option value="-1">镇/区</option>');
        }else if(areaType=='district'){
           $('#'+areaType).html('<option value="-1">镇/区</option>');
        }
        if(areaType!='null'){
            $.each(data,function(no,items){
                $('#'+areaType).append('<option value="'+items.region_id+'">'+items.region_name+'</option>');
            });
        }
    });
}