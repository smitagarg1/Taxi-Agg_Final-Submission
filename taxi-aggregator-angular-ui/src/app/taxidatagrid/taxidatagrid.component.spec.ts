import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TaxidatagridComponent } from './taxidatagrid.component';

describe('TaxidatagridComponent', () => {
  let component: TaxidatagridComponent;
  let fixture: ComponentFixture<TaxidatagridComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TaxidatagridComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TaxidatagridComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
