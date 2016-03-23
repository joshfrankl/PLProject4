"use strict";

var list = function() {
    var list = function () {
        function Node(data) {
            this.data = data;
            this.next = null;
        }

        var l = {
            length: 0,
            currentNode: null,
            head: new Node(null),
            add: function(e) {
                if (l.currentNode === null) { // This is true the first time
                    l.head.data = e;
                    l.currentNode = new Node(null);
                    l.head.next = l.currentNode;
                    l.length++;
                }
                else {
                    l.currentNode.data = e;
                    var node = new Node(null);
                    l.currentNode.next = node;
                    l.currentNode = node;
                    l.length++;
                }
            },
        };

        var F = function () {
        };
        var f = new F();

        // public data
        f.run = function (e) {
            return l[e];
        };
        f.first = f.car = function () {
            return l.head.data
        };
        f.rest = f.cdr = function () {
            if(l.length > 0) {
                l.head = l.head.next;
                l.length--;
            }
            return this;
        }
        f.concat = f.cons = function(e){
            if (typeof e === 'string' || e instanceof String) {l.add(e);}
            else {
                var n = e.run('head');
                for(var i = 0; i < e.run('length'); i++) {
                    l.add(n.data);
                    n = n.next;
                }
            }
        }
        f.length = function(){return l.length}
        f.map = function(f) {
            if (f instanceof Function) {
                var n = l.head;
                for(var i = 0; i < l.length; i++) {
                    n.data = f(n.data);
                    n = n.next;
                }
            }
        }
        f.iterate = function() {
            var current = l.head; // Keep track of last element returned
            var firstElement = true; // Prevents skipping over first element

            return {
                next: function() {
                    if (firstElement == true) { // Return the first element
                        firstElement = false;
                        return current.data;
                    }
                    else if (current.next.data != null) { // There is more to iterate over
                        current = current.next; // Move pointer to the next element
                        return current.data; // Return the next element
                    }
                    else { // Return null if at the end of the list
                        return null;
                    }
                }
            }
        }

        return f;
    }();
    return list;
};


// Create a new list l1 (x, y, z) in order to test iterator
var l1 = new list();
l1.cons('x');
l1.cons('y');
l1.cons('z');
var it = l1.iterate();
document.writeln("<BR>l1 iterate 1: " + it.next());
document.writeln("<BR>l1 iterate 2: " + it.next());
document.writeln("<BR>l1 iterate 3: " + it.next());
document.writeln("<BR>l1 iterate 4 (end of list - should be null): " + it.next());
l1.cons('a');
document.writeln("<BR>l1 iterate 5 (new node added): " + it.next());
document.writeln("<BR>l1 iterate 6 (end of list - should be null): " + it.next());