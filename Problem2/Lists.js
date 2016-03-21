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

var l1 = new list();
l1.concat('a')
l1.cons('b')
document.writeln("l1: " + l1.first() + "<BR>");
document.writeln("l1: " + l1.length() + "<BR>");

var l2 = new list();
l2.cons('c')
document.writeln("<BR>l2: " + l2.car() + "<BR>");
document.writeln("l2: " + l2.length() + "<BR>");

var l3 = new list();
var l4 = new list();
l3.cons('x')
l3.cons('y')
l3.cons('z')
l4.cons(l3);
l4.cons(l3.car());

document.writeln("<BR>l3: " + l3.car());
while(l3.length() > 0) {
    document.writeln(", " + l3.cdr().car());
}

var h = l4.run('head');
document.writeln("<BR>l4: " + h.data);
for(var i = 1; i < l4.length(); i++) {
    h = h.next;
    document.writeln(", " + h.data);
}

l4.map(function(x){return x+x;});
var h = l4.run('head');
document.writeln("<BR>l4 map: " + h.data);
for(var i = 1; i < l4.length(); i++) {
    h = h.next;
    document.writeln(", " + h.data);
}

// Create a new list l5 (x, y, z) in order to test iterator
var l5 = new list();
l5.cons('x')
l5.cons('y')
l5.cons('z')
document.writeln("<BR>");
var it = l5.iterate();
document.writeln("<BR>l5 iterate 1: " + it.next());
document.writeln("<BR>l5 iterate 2: " + it.next());
document.writeln("<BR>l5 iterate 3: " + it.next());
document.writeln("<BR>l5 iterate 4 (end of list - should be null): " + it.next());