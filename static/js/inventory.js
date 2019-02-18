var stockApp = angular.module('inventorymanagement', []);

stockApp.controller('InvemtoryManagementController', function($scope, $http) {

	$scope.append_table_data = function(data) {
    var ht='<thead> \
            <th>Product Name</th> \
            <th>Vendor</th> \
            <th>Batch Number</th> \
            <th>Batch Date</th> \
            <th>Quantity</th> \
            <th>MRP</th> \
            <th>Action</th> \
            </thead> \
            <tbody>';

    angular.forEach(data, function(value) {
        var product = '<td>' + value.product_name + '</td>'
        var vendor = '<td>' + value.vendor_name + '</td>'
        var batch_number = '<td>' + value.batch_number + '</td>'
        var batch_date = '<td>' + value.batch_date + '</td>'
        var quantity = '<td>' + value.quantity + '</td>'
        var mrp = '<td>' + value.mrp + '</td>'
        var action = '<td> \
                        <a href=/stock/inventory/' + value.id + '/edit><button class="btn btn-primary">Edit</button></a> \
                        <button class="btn btn-danger" Onclick="return ConfirmDelete(this, ' + value.id + ');">Delete</button>\
                       </td>'
        ht += '<tr>' +
                     product + vendor + batch_number + batch_date +
                     quantity + mrp + action +
              '</tr>'
      });
      ht = ht + '</tbody>';
      $('#stocklist').html(ht);
    }

     $scope.inventoryList = function() {
	     myTable = $('#stocklist tbody tr').remove();
	     $http({
	        method : "GET",
	        url : "/stock/get/inventory/data/",
	        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
	      }).then(function mySuccess(response) {
	          var response = response.data;
	          $scope.append_table_data(response)
	        }, function myError(response) {
	            alert("Unable to fetch data.")
	      });
   };

});