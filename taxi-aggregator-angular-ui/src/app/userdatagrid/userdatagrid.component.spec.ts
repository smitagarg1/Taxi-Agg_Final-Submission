import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UserdatagridComponent } from './userdatagrid.component';

describe('UserdatagridComponent', () => {
  let component: UserdatagridComponent;
  let fixture: ComponentFixture<UserdatagridComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UserdatagridComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(UserdatagridComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
