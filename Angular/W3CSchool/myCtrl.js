/**
 * Created by peter on 2016/8/16.
 */
app.controller('nameController', function($scope) {
    $scope.names = [
        {name:'Jani',country:'Norway'},
        {name:'Hege',country:'Sweden'},
        {name:'Kai',country:'Denmark'}
    ];
});

app.controller('personController', function($scope) {
    $scope.person = {
        firstName: "John",
        lastName: "Doe",
        fullName: function() {
            var x = $scope.person;
            return x.firstName + " " + x.lastName;
        }
    };
});