import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Sample data
menu = {
    "Coffee": ["Americano", "Cappuccino", "Latte"],
    "Tea": ["Black Tea", "Green Tea"],
    "Smoothie": ["Berry Blast", "Mango Magic"]
}
prices = {
    "Americano": 2500, "Cappuccino": 2700, "Latte": 2800,
    "Black Tea": 1900, "Green Tea": 1800,
    "Berry Blast": 3200, "Mango Magic": 3300
}
size_cost = {"Small": 0, "Medium": 50, "Large": 100}
addons_cost = {"Syrup": 300, "Extra Shot": 500, "Soy/Almond Milk": 400}


class BrewTimeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BrewTime Café")
        self.root.configure(bg="#E6F0FA")
        self.root.geometry("950x750")
        self.order_list = []

        # Color scheme
        self.primary_color = "#003087"
        self.secondary_color = "#D6EAF8"
        self.accent_color = "#0053A6"
        self.text_color = "#1C2526"

        # Configure root grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Sidebar frame
        sidebar_frame = tk.Frame(self.root, bg=self.primary_color, width=250)
        sidebar_frame.grid(row=0, column=0, sticky=(tk.N, tk.S))
        sidebar_frame.grid_rowconfigure(1, weight=1)

        # Welcome Section in sidebar
        tk.Label(
            sidebar_frame, text="BrewTime Café", font=("Arial", 20, "bold"),
            fg="white", bg=self.primary_color
        ).grid(row=0, column=0, pady=(10, 20), padx=10)
        self.menu_text = tk.Text(
            sidebar_frame, height=20, width=40, font=("Arial", 10),
            bg=self.secondary_color, fg=self.text_color, relief="flat"
        )
        self.menu_text.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.N, tk.S))
        self.update_menu_display()

        # Main content frame
        self.content_frame = tk.Frame(self.root, bg="#E6F0FA")
        self.content_frame.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        # Navigation buttons
        btn_frame = tk.Frame(sidebar_frame, bg=self.primary_color)
        btn_frame.grid(row=2, column=0, pady=10, padx=10, sticky=(tk.S))
        tk.Button(
            btn_frame, text="Order", command=self.show_customer_view, font=("Arial", 12, "bold"),
            bg="white", fg=self.primary_color, width=15, height=2, relief="flat",
            activebackground=self.accent_color, activeforeground="white"
        ).grid(row=0, column=0, pady=5)
        tk.Button(
            btn_frame, text="Admin", command=self.show_admin_login, font=("Arial", 12, "bold"),
            bg="white", fg=self.primary_color, width=15, height=2, relief="flat",
            activebackground=self.accent_color, activeforeground="white"
        ).grid(row=1, column=0, pady=5)

               

    def update_menu_display(self):
        """Update the menu display in the sidebar."""
        self.menu_text.delete(1.0, tk.END)
        for category, drinks in menu.items():
            self.menu_text.insert(tk.END, f"**{category}**\n", "category")
            for drink in sorted(drinks):
                self.menu_text.insert(tk.END, f"  - {drink}: {prices[drink]} CENTS\n")
            self.menu_text.insert(tk.END, "\n")
        self.menu_text.tag_configure("category", font=("Arial", 12, "bold"))

    def show_customer_view(self):
        """Display the customer order view."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        main_frame = tk.Frame(self.content_frame, bg="#E6F0FA", padx=20, pady=20)
        main_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Header
        header_frame = tk.Frame(main_frame, bg="#E6F0FA")
        header_frame.grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(
            header_frame, text="Pick a Drink", font=("Arial", 20, "bold"),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=0, column=0, padx=10)

        # Input Section
        input_frame = tk.Frame(main_frame, bg="#E6F0FA")
        input_frame.grid(row=1, column=0, sticky=(tk.N, tk.W), padx=10, pady=10)
        row = 0
        tk.Label(
            input_frame, text="Drink Category:", font=("Arial", 12),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=row, column=0, pady=5, sticky=tk.W)
        self.category_var = tk.StringVar()
        category_menu = ttk.Combobox(
            input_frame, textvariable=self.category_var, values=list(menu.keys()),
            font=("Arial", 12), width=20
        )
        category_menu.grid(row=row, column=1, pady=5, sticky=tk.W)
        category_menu.bind("<<ComboboxSelected>>", self.update_drinks)

        row += 1
        tk.Label(
            input_frame, text="Drink Type:", font=("Arial", 12),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=row, column=0, pady=5, sticky=tk.W)
        self.drink_var = tk.StringVar()
        self.drink_menu = ttk.Combobox(
            input_frame, textvariable=self.drink_var, font=("Arial", 12), width=20
        )
        self.drink_menu.grid(row=row, column=1, pady=5, sticky=tk.W)

        row += 1
        tk.Label(
            input_frame, text="Size:", font=("Arial", 12),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=row, column=0, pady=5, sticky=tk.W)
        self.size_var = tk.StringVar(value="Medium")
        size_menu = ttk.Combobox(
            input_frame, textvariable=self.size_var, values=list(size_cost.keys()),
            font=("Arial", 12), width=20
        )
        size_menu.grid(row=row, column=1, pady=5, sticky=tk.W)

        row += 1
        tk.Label(
            input_frame, text="Number of Cups:", font=("Arial", 12),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=row, column=0, pady=5, sticky=tk.W)
        self.cups_var = tk.IntVar(value=1)
        ttk.Entry(
            input_frame, textvariable=self.cups_var, font=("Arial", 12), width=10
        ).grid(row=row, column=1, pady=5, sticky=tk.W)

        row += 1
        tk.Label(
            input_frame, text="Add-ons:", font=("Arial", 12, "bold"),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=row, column=0, pady=5, sticky=tk.W)
        self.addons = {}
        addons_frame = tk.Frame(input_frame, bg="#E6F0FA")
        addons_frame.grid(row=row + 1, column=0, columnspan=2, pady=5)
        for i, (addon, cost) in enumerate(addons_cost.items()):
            var = tk.BooleanVar()
            tk.Checkbutton(
                addons_frame, text=f"{addon} (+{cost} CENTS)", variable=var,
                font=("Arial", 10), fg=self.text_color, bg="#E6F0FA",
                activebackground=self.secondary_color
            ).grid(row=i, column=0, pady=2, sticky=tk.W)
            self.addons[addon] = var

        # Order Summary Header
        header_frame = tk.Frame(main_frame, bg="#E6F0FA")
        header_frame.grid(row=18, column=0, columnspan=2, pady=10)
        tk.Label(
            header_frame, text="Order Summary", font=("Arial", 20, "bold"),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=0, column=0, padx=10)

        # Order Table
        table_frame = tk.Frame(main_frame, bg="#E6F0FA")
        table_frame.grid(row=19, column=0, sticky=(tk.N, tk.S, tk.E, tk.W), padx=10, pady=10)
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        columns = ("Drink", "Size", "Add-ons", "Qty", "Total (CENTS)")
        self.tree = ttk.Treeview(
            table_frame, columns=columns, show="headings", height=10
        )
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        style = ttk.Style()
        style.configure(
            "Custom.Treeview", background="#D6EAF8", foreground=self.text_color,
            fieldbackground="#0B0A11", font=("Arial", 10)
        )
        style.configure(
            "Custom.Treeview.Heading", background=self.primary_color,
            foreground="Black", font=("Arial", 10, "bold")
        )
        self.tree.configure(style="Custom.Treeview")

        # Buttons
        btn_frame = tk.Frame(main_frame, bg="#E6F0FA")
        btn_frame.grid(row=20, column=0, columnspan=2, pady=10, sticky=(tk.E))
        tk.Button(
            btn_frame, text="Add Order", command=self.add_order, font=("Arial", 10, "bold"),
            bg=self.primary_color, fg="white", width=12, height=2, relief="flat",
            activebackground=self.accent_color
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            btn_frame, text="Cancel Order", command=self.cancel_order, font=("Arial", 10, "bold"),
            bg=self.primary_color, fg="white", width=15, height=2, relief="flat",
            activebackground=self.accent_color
        ).grid(row=0, column=1, padx=5)
        tk.Button(
            btn_frame, text="Generate Voucher", command=self.generate_voucher,
            font=("Arial", 10, "bold"), bg=self.primary_color, fg="white", width=15,
            height=2, relief="flat", activebackground=self.accent_color
        ).grid(row=0, column=2, padx=5)

        def clear_data():
            """Clear all order data and reset the customer view."""
            self.order_list.clear()
            self.category_var.set("")
            self.drink_var.set("")
            self.size_var.set("Medium")
            self.cups_var.set(1)
            for addon in self.addons.values():
                addon.set(False)
            self.update_table()
            self.show_customer_view()

        tk.Button(
            btn_frame, text="Clear", command=clear_data, font=("Arial", 10, "bold"),
            bg=self.primary_color, fg="white", width=12, height=2, relief="flat",
            activebackground=self.accent_color
        ).grid(row=0, column=3, padx=5)

    def update_drinks(self, event):
        """Update drink options based on selected category."""
        category = self.category_var.get()
        if category in menu:
            self.drink_menu['values'] = menu[category]
            self.drink_var.set(menu[category][0] if menu[category] else "")

    def add_order(self):
        """Add a new order to the order list."""
        drink = self.drink_var.get()
        size = self.size_var.get()
        qty = self.cups_var.get()
        if qty <= 0:
            messagebox.showwarning("Warning", "Number of cups must be positive!")
            return
        addons_selected = [addon for addon, var in self.addons.items() if var.get()]
        addons_str = ", ".join(addons_selected) if addons_selected else "None"
        addons_cost_total = sum(addons_cost[addon] for addon in addons_selected)

        if drink not in prices:
            messagebox.showwarning("Warning", "Invalid drink selection!")
            return

        base_price = prices[drink]
        size_cost_total = size_cost.get(size, 0)
        item_total = (base_price + size_cost_total + addons_cost_total) * qty
        self.order_list.append((drink, size, addons_str, qty, item_total))
        self.update_table()

    def update_table(self):
        """Update the order table display."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for item in self.order_list:
            self.tree.insert("", tk.END, values=item)

    def cancel_order(self):
        """Cancel selected orders."""
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("Warning", "Please select an item to cancel!")
            return
        if messagebox.askyesno("Confirm", "Are you sure you want to cancel the selected item(s)?"):
            selected_indices = sorted([self.tree.index(item) for item in selected_items], reverse=True)
            for index in selected_indices:
                if 0 <= index < len(self.order_list):
                    del self.order_list[index]
            self.update_table()

    def generate_voucher(self):
        """Generate and display the order voucher."""
        if not self.order_list:
            messagebox.showwarning("Warning", "No orders to generate voucher!")
            return
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d %H:%M:%S")

        voucher = tk.Toplevel(self.root)
        voucher.title("BrewTime Café Voucher")
        voucher.configure(bg="#E6F0FA")
        voucher.geometry("500x700")
        voucher.grid_rowconfigure(0, weight=1)
        voucher.grid_columnconfigure(0, weight=1)

        main_frame = tk.Frame(voucher, bg="#E6F0FA", padx=20, pady=20)
        main_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        tk.Label(
            main_frame, text="BrewTime Café Voucher", font=("Arial", 22, "bold"),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=0, column=0, pady=10)
        tk.Label(
            main_frame, text=f"Date: {date_str}", font=("Arial", 10, "italic", "bold"),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=1, column=0, pady=5)

        detail_frame = tk.Frame(main_frame, bg="#E6F0FA")
        detail_frame.grid(row=2, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        detail_frame.grid_rowconfigure(0, weight=1)
        detail_frame.grid_columnconfigure(0, weight=1)
        canvas = tk.Canvas(detail_frame, bg="#E6F0FA")
        canvas.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        scrollbar = tk.Scrollbar(detail_frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        inner_frame = tk.Frame(canvas, bg="#E6F0FA")
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        grand_total = 0
        row = 0
        for idx, (drink, size, addons_str, qty, item_total) in enumerate(self.order_list, 1):
            tk.Label(
                inner_frame, text=f"{idx}. {drink} ({size}) x {qty}", font=("Arial", 12),
                fg=self.text_color, bg="#E6F0FA"
            ).grid(row=row, column=0, padx=10, pady=2, sticky=tk.W)
            row += 1
            base_price = prices[drink] * qty
            tk.Label(
                inner_frame, text="Base Price:", font=("Arial", 10),
                fg=self.text_color, bg="#E6F0FA"
            ).grid(row=row, column=0, padx=20, pady=2, sticky=tk.W)
            tk.Label(
                inner_frame, text=f"{base_price} CENTS", font=("Arial", 10),
                fg=self.text_color, bg="#E6F0FA"
            ).grid(row=row, column=1, padx=20, pady=2, sticky=tk.E)
            row += 1
            size_c = size_cost[size] * qty
            if size_c > 0:
                tk.Label(
                    inner_frame, text=f"Size ({size}):", font=("Arial", 10),
                    fg=self.text_color, bg="#E6F0FA"
                ).grid(row=row, column=0, padx=20, pady=2, sticky=tk.W)
                tk.Label(
                    inner_frame, text=f"{size_c} CENTS", font=("Arial", 10),
                    fg=self.text_color, bg="#E6F0FA"
                ).grid(row=row, column=1, padx=20, pady=2, sticky=tk.E)
                row += 1
            addons_list = addons_str.split(", ") if addons_str != "None" else []
            addons_c = sum(addons_cost[addon] for addon in addons_list) * qty
            if addons_c > 0:
                tk.Label(
                    inner_frame, text=f"+ {addons_str}:", font=("Arial", 10),
                    fg=self.text_color, bg="#E6F0FA"
                ).grid(row=row, column=0, padx=20, pady=2, sticky=tk.W)
                tk.Label(
                    inner_frame, text=f"{addons_c} CENTS", font=("Arial", 10),
                    fg=self.text_color, bg="#E6F0FA"
                ).grid(row=row, column=1, padx=20, pady=2, sticky=tk.E)
                row += 1
            tk.Label(
                inner_frame, text="Item Total:", font=("Arial", 12, "bold"),
                fg=self.text_color, bg="#E6F0FA"
            ).grid(row=row, column=0, padx=20, pady=2, sticky=tk.W)
            tk.Label(
                inner_frame, text=f"{item_total} CENTS", font=("Arial", 12, "bold"),
                fg=self.text_color, bg="#E6F0FA"
            ).grid(row=row, column=1, padx=20, pady=2, sticky=tk.E)
            row += 1
            grand_total += item_total

        tk.Label(
            main_frame, text=f"Total: {grand_total} CENTS", font=("Arial", 16, "bold"),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=4, column=0, pady=10)
        tk.Label(
            main_frame, text="Thank you for your order!", font=("Arial", 12),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=5, column=0, pady=10)

        btn_frame = tk.Frame(main_frame, bg="#E6F0FA")
        btn_frame.grid(row=6, column=0, pady=10)
        tk.Button(
            btn_frame, text="Back", command=voucher.destroy, font=("Arial", 12, "bold"),
            bg=self.primary_color, fg="white", width=10, height=2, relief="raised",
            activebackground=self.accent_color
        ).grid(row=0, column=0, padx=5)

        def voucher_close():
            """Close the voucher and reset order data."""
            self.order_list.clear()
            self.category_var.set("")
            self.drink_var.set("")
            self.size_var.set("Medium")
            self.cups_var.set(1)
            for addon in self.addons.values():
                addon.set(False)
            self.update_table()
            voucher.destroy()
            self.show_customer_view()

        tk.Button(
            btn_frame, text="Close", command=voucher_close, font=("Arial", 12, "bold"),
            bg=self.primary_color, fg="white", width=10, height=2, relief="raised",
            activebackground=self.accent_color
        ).grid(row=0, column=1, padx=5)

    def show_admin_login(self):
        """Display the admin login view."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        login = tk.Frame(self.content_frame, bg="#E6F0FA", padx=20, pady=20)
        login.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        login.grid_rowconfigure(3, weight=1)
        login.grid_columnconfigure(1, weight=1)

        tk.Label( 
            login, text="Admin Login", font=("Arial", 18, "bold"),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(
            login, text="Username:", font=("Arial", 14),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=1, column=0, pady=10, sticky=tk.W)
        self.username_var = tk.StringVar()
        ttk.Entry(
            login, textvariable=self.username_var, font=("Arial", 12), width=20
        ).grid(row=1, column=1, pady=10, sticky=tk.W)
        tk.Label(
            login, text="Password:", font=("Arial", 14),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=2, column=0, pady=10, sticky=tk.W)
        self.password_var = tk.StringVar()
        ttk.Entry(
            login, textvariable=self.password_var, show="*", font=("Arial", 12), width=20
        ).grid(row=2, column=1, pady=10, sticky=tk.W)

        btn_frame = tk.Frame(login, bg="#E6F0FA")
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(
            btn_frame, text="Login", command=lambda: self.login_admin(login),
            font=("Arial", 12, "bold"), bg=self.primary_color, fg="white", width=10,
            height=1, relief="flat", activebackground=self.accent_color
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            btn_frame, text="Back", command=self.show_customer_view, font=("Arial", 12, "bold"),
            bg=self.primary_color, fg="white", width=10, height=1, relief="flat",
            activebackground=self.accent_color
        ).grid(row=0, column=1, padx=5)

    def login_admin(self, login_frame):
        """Handle admin login authentication with input validation using try-except."""
        try:
            username = self.username_var.get().strip()
            password = self.password_var.get().strip()

            # Check for non-empty fields
            if not username or not password:
                raise ValueError("Please fill in both username and password!")

            # Validate credentials
            if username == "admin" and password == "admin123":
                self.show_admin_panel()
            else:
                raise ValueError("Invalid username or password!")

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def show_admin_panel(self):
        """Display the admin panel view."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        admin = tk.Frame(self.content_frame, bg="#E6F0FA", padx=20, pady=20)
        admin.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        admin.grid_rowconfigure(0, weight=1)
        admin.grid_columnconfigure(1, weight=1)

        table_frame = tk.Frame(admin, bg="#E6F0FA")
        table_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.N, tk.S, tk.E, tk.W))
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        columns = ("Category", "Drink", "Price (CENTS)")
        self.admin_tree = ttk.Treeview(
            table_frame, columns=columns, show="headings", height=15
        )
        for col in columns:
            self.admin_tree.heading(col, text=col)
            self.admin_tree.column(col, width=150)
        self.admin_tree.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        style = ttk.Style()
        style.configure(
            "Custom.Treeview", background="#D6EAF8", foreground=self.text_color,
            fieldbackground="#D6EAF8", font=("Arial", 12)
        )
        style.configure(
            "Custom.Treeview.Heading", background=self.primary_color,
            foreground="Blue", font=("Arial", 12, "bold", "italic")
        )
        self.admin_tree.configure(style="Custom.Treeview")
        self.update_admin_table()

        btn_frame = tk.Frame(admin, bg="#E6F0FA")
        btn_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.E))
        tk.Button(
            btn_frame, text="New", command=self.add_drink_window, font=("Arial", 12, "bold"),
            bg=self.primary_color, fg="white", width=10, height=2, relief="flat",
            activebackground=self.accent_color
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            btn_frame, text="Update", command=self.edit_drink_window,
            font=("Arial", 12, "bold"), bg=self.primary_color, fg="white", width=10,
            height=2, relief="flat", activebackground=self.accent_color
        ).grid(row=0, column=1, padx=5)
        tk.Button(
            btn_frame, text="Delete", command=self.delete_drink,
            font=("Arial", 12, "bold"), bg=self.primary_color, fg="white", width=10,
            height=2, relief="flat", activebackground=self.accent_color
        ).grid(row=0, column=2, padx=5)
        tk.Button(
            btn_frame, text="Close", command=self.root.destroy, font=("Arial", 12, "bold"),
            bg=self.primary_color, fg="white", width=10, height=2, relief="flat",
            activebackground=self.accent_color
        ).grid(row=0, column=3, padx=5)

    def update_admin_table(self):
        """Update the admin table display."""
        for item in self.admin_tree.get_children():
            self.admin_tree.delete(item)
        for category in sorted(menu.keys()):
            for drink in sorted(menu[category]):
                self.admin_tree.insert("", tk.END, values=(category, drink, prices[drink]))

    def add_drink_window(self):
        """Open window to add a new drink."""
        add_win = tk.Toplevel(self.root)
        add_win.title("Add New Drink")
        add_win.configure(bg="#E6F0FA")
        add_win.geometry("400x300")
        add_win.grid_rowconfigure(0, weight=1)
        add_win.grid_columnconfigure(1, weight=1)

        main_frame = tk.Frame(add_win, bg="#E6F0FA", padx=20, pady=20)
        main_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        row = 0
        tk.Label(
            main_frame, text="Category:", font=("Arial", 12),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=row, column=0, pady=10, sticky=tk.W)
        category_var = tk.StringVar()
        ttk.Entry(
            main_frame, textvariable=category_var, font=("Arial", 12), width=25
        ).grid(row=row, column=1, pady=10, sticky=tk.W)

        row += 1
        tk.Label(
            main_frame, text="Drink:", font=("Arial", 12),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=row, column=0, pady=10, sticky=tk.W)
        drink_var = tk.StringVar()
        ttk.Entry(
            main_frame, textvariable=drink_var, font=("Arial", 12), width=25
        ).grid(row=row, column=1, pady=10, sticky=tk.W)

        row += 1
        tk.Label(
            main_frame, text="Price (CENTS):", font=("Arial", 12),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=row, column=0, pady=10, sticky=tk.W)
        price_var = tk.StringVar()
        ttk.Entry(
            main_frame, textvariable=price_var, font=("Arial", 12), width=25
        ).grid(row=row, column=1, pady=10, sticky=tk.W)

        btn_frame = tk.Frame(main_frame, bg="#E6F0FA")
        btn_frame.grid(row=row + 1, column=0, columnspan=2, pady=10)
        tk.Button(
            btn_frame, text="Add", command=lambda: self.add_drink(category_var, drink_var, price_var, add_win),
            font=("Arial", 12, "bold"), bg=self.primary_color, fg="white", width=10,
            height=2, relief="flat", activebackground=self.accent_color
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            btn_frame, text="Cancel", command=add_win.destroy, font=("Arial", 12, "bold"),
            bg=self.primary_color, fg="white", width=10, height=2, relief="flat",
            activebackground=self.accent_color
        ).grid(row=0, column=1, padx=5)

    def add_drink(self, category_var, drink_var, price_var, add_win):
        """Add a new drink to the menu."""
        cat = category_var.get().strip()
        dr = drink_var.get().strip()
        try:
            pr = int(price_var.get())
            if pr <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Warning", "Price must be a positive integer!")
            return
        if cat and dr:
            if dr in prices:
                messagebox.showerror("Error", "Drink already exists!")
                return
            if cat not in menu:
                menu[cat] = []
            menu[cat].append(dr)
            prices[dr] = pr
            self.update_admin_table()
            self.update_menu_display()
            add_win.destroy()
            messagebox.showinfo("Success", "Drink added successfully!")
        else:
            messagebox.showwarning("Warning", "Please fill all fields!")

    def edit_drink_window(self):
        """Open window to edit a selected drink."""
        selected = self.admin_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a drink to edit!")
            return
        item = self.admin_tree.item(selected[0])["values"]
        old_cat, old_dr, old_pr = item

        edit_win = tk.Toplevel(self.root)
        edit_win.title("Edit Drink")
        edit_win.configure(bg="#E6F0FA")
        edit_win.geometry("400x300")
        edit_win.grid_rowconfigure(0, weight=1)
        edit_win.grid_columnconfigure(1, weight=1)

        main_frame = tk.Frame(edit_win, bg="#E6F0FA", padx=20, pady=20)
        main_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        row = 0
        tk.Label(
            main_frame, text="Category:", font=("Arial", 12),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=row, column=0, pady=10, sticky=tk.W)
        category_var = tk.StringVar(value=old_cat)
        ttk.Entry(
            main_frame, textvariable=category_var, font=("Arial", 12), width=25
        ).grid(row=row, column=1, pady=10, sticky=tk.W)

        row += 1
        tk.Label(
            main_frame, text="Drink:", font=("Arial", 12),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=row, column=0, pady=10, sticky=tk.W)
        drink_var = tk.StringVar(value=old_dr)
        ttk.Entry(
            main_frame, textvariable=drink_var, font=("Arial", 12), width=25
        ).grid(row=row, column=1, pady=10, sticky=tk.W)

        row += 1
        tk.Label(
            main_frame, text="Price (CENTS):", font=("Arial", 12),
            fg=self.text_color, bg="#E6F0FA"
        ).grid(row=row, column=0, pady=10, sticky=tk.W)
        price_var = tk.StringVar(value=str(old_pr))
        ttk.Entry(
            main_frame, textvariable=price_var, font=("Arial", 12), width=25
        ).grid(row=row, column=1, pady=10, sticky=tk.W)

        btn_frame = tk.Frame(main_frame, bg="#E6F0FA")
        btn_frame.grid(row=row + 1, column=0, columnspan=2, pady=10)
        tk.Button(
            btn_frame, text="Update", command=lambda: self.update_drink(category_var, drink_var, price_var, old_cat, old_dr, edit_win),
            font=("Arial", 12, "bold"), bg=self.primary_color, fg="white", width=10,
            height=2, relief="flat", activebackground=self.accent_color
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            btn_frame, text="Cancel", command=edit_win.destroy, font=("Arial", 12, "bold"),
            bg=self.primary_color, fg="white", width=10, height=2, relief="flat",
            activebackground=self.accent_color
        ).grid(row=0, column=1, padx=5)

    def update_drink(self, category_var, drink_var, price_var, old_cat, old_dr, edit_win):
        """Update an existing drink in the menu."""
        new_cat = category_var.get().strip()
        new_dr = drink_var.get().strip()
        try:
            new_pr = int(price_var.get())
            if new_pr <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Warning", "Price must be a positive integer!")
            return
        if new_cat and new_dr:
            if new_dr != old_dr and new_dr in prices:
                messagebox.showerror("Error", "Drink name already exists!")
                return
            menu[old_cat].remove(old_dr)
            if not menu[old_cat]:
                del menu[old_cat]
            if new_cat not in menu:
                menu[new_cat] = []
            menu[new_cat].append(new_dr)
            if new_dr != old_dr:
                del prices[old_dr]
            prices[new_dr] = new_pr
            self.update_admin_table()
            self.update_menu_display()
            edit_win.destroy()
            messagebox.showinfo("Success", "Drink updated successfully!")
        else:
            messagebox.showwarning("Warning", "Please fill all fields!")

    def delete_drink(self):
        """Delete a selected drink from the menu."""
        selected = self.admin_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a drink to delete!")
            return
        item = self.admin_tree.item(selected[0])["values"]
        cat, dr, _ = item
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this drink?"):
            menu[cat].remove(dr)
            if not menu[cat]:
                del menu[cat]
            del prices[dr]
            self.update_admin_table()
            self.update_menu_display()
            messagebox.showinfo("Success", "Drink deleted successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    app = BrewTimeApp(root)
    root.mainloop()