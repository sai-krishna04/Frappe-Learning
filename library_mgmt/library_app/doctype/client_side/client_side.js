frappe.ui.form.on("client_side", {
    refresh(frm) {
        frm.call("frm_call", {
            msg: "Hello"
        }).then((r) => {
            frappe.msgprint(r.message);
        });
    },

    // onload(frm){
    //     frappe.throw("Hello from onload method");
    // }

    // validate(frm) {
    //     // frappe.throw("Hello from validate method");
    //     frm.set_value("full",frm.doc.name1 + " " +frm.doc.last);

    //     let row=frm.add_child("child",{
    //         name1:"Krishna",
    //         age:21,
    //     });

    // },
    
    // after_save(frm) {
    //     frappe.msgprint(__("Hello the user name is {0}", [frm.doc.name1]));

    //     for(let row of frm.doc.child){
    //         frappe.msgprint(__("Hello the child name is {0} and age is {1}", [row.name1, row.age]));
    //     }
    // }
    refresh(frm) {
        frm.set_intro("You can create new doc");

        frm.add_custom_button("Click Me1", () => {
            frappe.msgprint("Hello from custom button");
        },'click me')
        frm.add_custom_button("Click Me2", () => {
            frappe.msgprint("Hello from custom button 2");
        },'click me')
    }

    
});
// frappe.ui.form.on("Child Doc",{
//     name1(frm, cdt, cdn){
//         frappe.msgprint("Hello from child doctype");
//     },
//     age(frm, cdt, cdn){
//         frappe.msgprint("Hello from child doctype age field");
//     }
// })