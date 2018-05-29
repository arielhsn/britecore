(function() {
    'use strict';

    function requestViewModel() {
        var self = this;
    
        self.showMain = ko.observable(true);
        self.requestList = ko.observableArray();
        self.productAreaList = ko.observableArray();
        self.selectedProductArea = ko.observable();
        self.clientList = ko.observableArray();
        self.selectedClient = ko.observable();
        
        self.id = ko.observable();
        self.title = ko.observable();
        self.description = ko.observable();
        self.client_id = ko.observable();
        self.client_priority = ko.observable();
        self.target_date = ko.observable();
        self.product_area_id = ko.observable();

        self.clearForm = function() {
            self.id(null);
            self.title(null);
            self.description(null);
            self.client_id(null);
            self.client_priority(null);
            self.target_date(null);
            self.product_area_id(null);
        }

        $.getJSON('http://127.0.0.1:5000/product_area', function(data) {
            self.productAreaList(data.product_areas);
        });

        $.getJSON('http://127.0.0.1:5000/client', function(data) {
            self.clientList(data.clients);
        });

        self.getRequest = function() {
            $.getJSON('http://127.0.0.1:5000/request', function(data) {
                self.requestList(data.requests);
            });
        }

        self.saveRequest = function() {
            $.ajax({
                type: 'POST',
                url: 'http://127.0.0.1:5000/request',
                contentType: 'application/json',
                data: JSON.stringify({
                    id: self.id(),
                    title: self.title(),
                    description: self.description(),
                    client_id: self.client_id().id,
                    client_priority: self.client_priority(),
                    target_date: self.target_date(),
                    product_area_id: self.product_area_id().id
                })
            })
            .done(function (response, textStatus, jqXHR){
                self.clearForm();
                self.getRequest();
                self.showMain(true);
            })
            .fail(function (jqXHR, textStatus, errorThrown){
                console.error('Error: ' + textStatus, errorThrown);
            });
        }

        self.addRequest = function() {
            self.showMain(false);
        }

        self.cancel = function() {
            self.showMain(true);
        }

        self.formatTargetDate = function() {

            if (!self.target_date()) {
                return;
            }

            var dateFormated = self.target_date();

            dateFormated = dateFormated.replace(/\D/g, '');
            dateFormated = dateFormated.replace(/^(\d{4})(\d)/g, '$1-$2');
            dateFormated = dateFormated.replace(/(\d)(\d{2})$/g, '$1-$2');

            self.target_date(dateFormated);
        }

        self.formatClientPriority = function() {

            if (!self.client_priority()) {
                return;
            }

            var onlyNumber = self.client_priority();

            onlyNumber = onlyNumber.replace(/\D/g, '');

            self.client_priority(onlyNumber);
        }

        self.getRequest();
    }

    $(document).ready(function () {
        ko.applyBindings(new requestViewModel());
        // $('#target_date').keyup(function() {
        //     console.log(this);
        // });
    });
})();