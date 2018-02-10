var app = angular.module('CatApp',[]);
app.config(function($interpolateProvider, $httpProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    });
app.controller('catController', function($scope, $http){
    $http.get('/api/').then(function(response) {
    $scope.catList = [];
    for (var i = 0; i < response.data.length; i++){
        var cat = {};
        cat.user = response.data[i].user;
        cat.name = response.data[i].name;
        console.log(cat.name);
        cat.years = response.data[i].years;
        cat.breed = response.data[i].breed;
        cat.img = response.data[i].img;
        $scope.catList.push(cat);
    }});


});
