import base_function
import plot_function


if __name__ == '__main__': 
    print('-----')
    input_discount_rate=input('Discount Rate: ')
    discount_rate = float(input_discount_rate)
    print('-----')
    print('Input first cash flow, separate each cash flow by ",". ')
    print('    For example: -1100000, 500000, 300000, 300000, 300000 ')
    input_first_cash_flow=input('Cash flow: ')
    input_first_cash_flow_list=input_first_cash_flow.split(",")
    first_cash_flow = [int(input_first_cash_flow_list[i]) for i in range(len(input_first_cash_flow_list))]
    print('-----')
    print('Input second cash flow, separate each cash flow by ",". ')
    print('    For example: -150000, 80000, 80000, 30000, 10000, 20000')
    print('    (press [Enter] to Skip)')
    input_second_cash_flow=input('Cash flow: ')
    if input_second_cash_flow == '':
        input_second_cash_flow = '0,0'
    input_second_cash_flow_list=input_second_cash_flow.split(",")
    second_cash_flow = [int(input_second_cash_flow_list[i]) for i in range(len(input_second_cash_flow_list))]


    print('--------------------------------------------------------------------')
    print('--------------------------------------------------------------------')
    print('First Cash Flows: ',first_cash_flow)
    print('Discount Rate: ','\t\t\t',discount_rate)
    if base_function.payback_period(first_cash_flow) == -1:
        print('Payback Period (PP): ','\t\t\t','nan')
    else:
        print('Payback Period (PP): ','\t\t\t',format(base_function.payback_period(first_cash_flow), '.3f'))
    if base_function.discounted_payback_period(first_cash_flow, discount_rate) == -1:
        print('Discounted Payback Period (DPP): ','\t','nan')
    else:
        print('Discounted Payback Period (DPP): ','\t',format(base_function.discounted_payback_period(first_cash_flow, discount_rate), '.3f'))
    print('Net Present Value (NPV): ','\t\t',format(base_function.net_present_value(first_cash_flow, discount_rate), '.2f'))
    if base_function.equivalent_annual_annuity(first_cash_flow, discount_rate) == -1:
        print('Equivalent Annual Annuity (EAA): ','\t','nan')
    else:
        print('Equivalent Annual Annuity (EAA): ','\t',format(base_function.equivalent_annual_annuity(first_cash_flow, discount_rate), '.2f'))
    print('Internal Rate of Return (IRR): ','\t',format(base_function.internal_rate_of_return(first_cash_flow), '.4f'))
    print('Profitability Index (PI): ','\t\t',format(base_function.profitability_index(first_cash_flow, discount_rate), '.2f'))
    first_irr, second_irr, diff_cash_flow_irr, df_npv = base_function.npv_profile(first_cash_flow, second_cash_flow)
    
    if input_second_cash_flow != '0,0':
        print('--------------------------------------------------------------------')
        print('--------------------------------------------------------------------')
        print('Second Cash Flows: ',second_cash_flow)
        print('Discount Rate: ','\t\t\t',discount_rate)
        if base_function.payback_period(second_cash_flow) == -1:
            print('Payback Period (PP): ','\t\t\t','nan')
        else:
            print('Payback Period (PP): ','\t\t\t',format(base_function.payback_period(second_cash_flow), '.3f'))
        if base_function.discounted_payback_period(second_cash_flow, discount_rate) == -1:
            print('Discounted Payback Period (DPP): ','\t','nan')
        else:
            print('Discounted Payback Period (DPP): ','\t',format(base_function.discounted_payback_period(second_cash_flow, discount_rate), '.3f'))
        print('Net Present Value (NPV): ','\t\t',format(base_function.net_present_value(second_cash_flow, discount_rate), '.2f'))
        if base_function.equivalent_annual_annuity(second_cash_flow, discount_rate) == -1:
            print('Equivalent Annual Annuity (EAA): ','\t','nan')
        else:
            print('Equivalent Annual Annuity (EAA): ','\t',format(base_function.equivalent_annual_annuity(second_cash_flow, discount_rate), '.2f'))
        print('Internal Rate of Return (IRR): ','\t',format(base_function.internal_rate_of_return(second_cash_flow), '.4f'))
        print('Profitability Index (PI): ','\t\t',format(base_function.profitability_index(second_cash_flow, discount_rate), '.2f'))
        print('--------------------------------------------------------------------')
    
    print('Crossover Rate: ','\t\t\t',format(diff_cash_flow_irr, '.4f'))
    print('--------------------------------------------------------------------')
    plot_function.plot_npv_profile(first_cash_flow, second_cash_flow)