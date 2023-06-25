document.addEventListener('DOMContentLoaded', () => {
    const addExpenseBtn = document.getElementById('addExpenseBtn');
    const budgetForm = document.getElementById('budgetForm');
    const calculateBtn = document.getElementById('calculateBtn');
    const resultSection = document.getElementById('result');
    const totalExpense = document.getElementById('totalExpense');
    const calculationTime = document.getElementById('calculationTime');
    const printBtn = document.getElementById('printBtn');
    const expensesContainer = document.getElementById('expensesContainer');

    const budget_title = document.getElementById('budget_title');
    const budget_income = document.getElementById('budget_income');
    const all_expenses = document.getElementById('all_expenses');
    const all_costs = document.getElementById('all_costs');
    const total_cost = document.getElementById('total_cost');

    let expenseCount = 1;

    addExpenseBtn.addEventListener('click', () => {
      const expenseDiv = document.createElement('div');
      expenseDiv.classList.add('expense');

      const expenseNameInput = document.createElement('input');
      expenseNameInput.type = 'text';
      expenseNameInput.classList.add('expenseName');
      expenseNameInput.placeholder = 'Expense Name';
      expenseNameInput.required = true;

      const expensePriceInput = document.createElement('input');
      expensePriceInput.type = 'number';
      expensePriceInput.classList.add('expensePrice');
      expensePriceInput.placeholder = 'Price';
      expensePriceInput.required = true;

      expenseDiv.appendChild(expenseNameInput);
      expenseDiv.appendChild(expensePriceInput);

      expensesContainer.appendChild(expenseDiv);
      expenseCount++;
    });

    budgetForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const budgetName = document.getElementById('budgetName').value;
      const income = parseFloat(document.getElementById('income').value);
      const expenses = Array.from(document.getElementsByClassName('expense'));

      let totalExpensesCost = 0;
      let all_expense = "";
      let all_cost = "";

      expenses.forEach((expense) => {
        const expenseName = expense.querySelector('.expenseName').value;
        const expensePrice = parseFloat(expense.querySelector('.expensePrice').value);
        all_expense += `${ expenseName },`;
        all_cost += `${ expensePrice },`;
        totalExpensesCost += expensePrice;
      });

      total_cost.value = totalExpensesCost;

      let budget = income - totalExpensesCost;
      let budgetMessage = '';
      if (budget < 0) {
        budgetMessage = `You need an additional ${Math.abs(budget).toFixed(2)} to balance the budget.`;
      } else {
        budgetMessage = `Budget is balanced.`;
      }

      const currentTime = new Date().toLocaleString();

      totalExpense.textContent = `Total Expense: ${totalExpensesCost.toFixed(2)}`;
      calculationTime.textContent = `Calculation Time: ${currentTime}\n${budgetMessage}`;
      resultSection.classList.remove('hidden');
      printBtn.classList.remove('hidden');

      budget_title.value = budgetName;
      budget_income.value = income;
      all_costs.value = all_cost;
    all_expenses.value = all_expense;
  
      document.body.classList.add('animated', 'fadeIn');
    });
  
    printBtn.addEventListener('click', () => {
      window.print();
    });
  });

  //Login
  document.addEventListener('DOMContentLoaded', () => {
    const toggleForm = document.getElementById('toggleForm');
    const toggleText = document.getElementById('toggleText');
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
  
    toggleForm.addEventListener('click', (e) => {
      e.preventDefault();
      loginForm.classList.toggle('hidden');
      registerForm.classList.toggle('hidden');
  
      if (loginForm.classList.contains('hidden')) {
        toggleForm.textContent = "Login";
        toggleText.textContent = "Already have an account? ";
      } else {
        toggleText.textContent = "Don't have an account? ";
        toggleForm.textContent = "Register";
      }
    });
  });
  