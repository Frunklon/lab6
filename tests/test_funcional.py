import pytest
from src.manager import Manager
from src.models import Parameters


def test_total_due_pln():
    manager = Manager(Parameters())

    apartment_settlement = manager.get_settlement('apart-polanka', 2025, 1)

    assert apartment_settlement is not None

    tenant_settlements = manager.create_tenants_settlements(apartment_settlement)

    assert isinstance(tenant_settlements, list)
    assert len(tenant_settlements) > 0

    tenants_total_due = sum(tenant.total_due_pln
           
            for tenant in tenant_settlements)
   
   
   
    apartment_costs = manager.get_apartment_costs('apart-polanka', 2025, 1)

    assert tenants_total_due == apartment_settlement.total_due_pln
    assert tenants_total_due == apartment_costs


def test_check_deposits():
    params = Parameters(
        apartments_json_path="data/apartments.json",
        tenants_json_path="data/tenants.json",
        transfers_json_path="data/transfers.json",
        bills_json_path="data/bills.json"
    )

    manager = Manager(params)

    result = manager.check_deposit()

    assert result is False


def test_get_annual_report():

    manager = Manager(Parameters())

    report = manager.get_annual_report(2025)

    assert report["year"] == 2025
    assert report["total_costs"] == 910
    assert report["total_income"] == 7500
    assert report["balance"] == 6590
