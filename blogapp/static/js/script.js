var app = angular.module('CatApp',['ngMaterial', 'Authentication']);
app.config(function($interpolateProvider, $httpProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    });
app.controller('catController', function($scope, $http, $mdDialog){
    $http.get('/api/cat/').then(function(response) {
    $scope.catList = [];
    console.log(response.data);
    for (var i = 0; i < response.data.length; i++){
        var cat = {};
        cat.user = response.data[i].user;
        cat.name = response.data[i].name;
        cat.years = response.data[i].years;
        cat.breed = response.data[i].breed;
        cat.img = response.data[i].img;
        $scope.catList.push(cat);
    }});
    $scope.editCat = function(cat){
        if (cat) {
        $scope.catObj = cat;
        $mdDialog.show({
        contentElement: '#editCatDialog',
        parent: angular.element(document.body)
      });

        }
        else {
            $mdDialog.show({
            contentElement: '#editCatDialog',
            parent: angular.element(document.body)
            })
        }
      }
    $scope.closeDialog = function() {
          $mdDialog.hide();
    };

    $scope.saveEditDialog = function(catObj) {

        $http.post('api/', catObj)
    }


});
