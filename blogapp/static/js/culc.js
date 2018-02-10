
//Наши кнопки
        let signs = ['AC','(',')','÷','7','8','9','x','4','5','6','-','1','2','3','+','0',',','=']
         $(document).ready(function(){
            var inputVal = $('#calc_value');
            inputVal.val('0');
            //Добавление кнопок с помощью jQuery
            for (var i=0; i<signs.length; i++) {
                //отдельный случай с нулем (ширина в 2 раза больше)
                if (i==16) {
                    $('#calc').append('<div class="btn" id="zero">'+signs[i]+'</div>');
                    continue;
                }
                //Добавление класса orang_btn к оранжевым кнопкам
                var orang_btns = [3,7,11,15,18];
                if (orang_btns.indexOf(i) > -1) {
                    $('#calc').append('<div class="btn orang_btn" >'+signs[i]+'</div>');
                } else {
                    $('#calc').append('<div class="btn">'+signs[i]+'</div>');
                }

            };
            //действие при нажатии
            $('.btn').click(function(){
                if (inputVal.val() == '0') {
                    inputVal.val('');
                };
                //считываем пример
                inputVal = $('#calc_value');
                var calculations = $('#calculations'); //переменная для отображения сверху ответа последние действия
                if (this.innerHTML == 'AC') {
                    inputVal.val('0');
                    calculations.text('');
                } else if (this.innerHTML == 'x') {
                    inputVal.val(inputVal.val() + '*')
                } else if (this.innerHTML == '=') {
                    var inp_str = inputVal.val();
                    calculations.text(inp_str + '=');
                    inp_str = inp_str.replace(/÷/g,"/");  //замена символом, чтоб функция eval() заработала
                    inp_str = inp_str.replace(/,/g,".");
                    value_with_dote = Math.round(eval(inp_str) * 100) / 100 ;
                    inputVal.val(value_with_dote);


                } else {
                    inputVal.val(inputVal.val() + this.innerHTML);
                    //изменение размера цифр
                    if (inputVal.val().length > 9) {
                        inputVal.css('font-size', '20px');
                    } else {
                        inputVal.css('font-size', '30px');
                    }
                }


         });
        });
