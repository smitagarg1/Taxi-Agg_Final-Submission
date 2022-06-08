import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LocationchartComponent } from './locationchart.component';

describe('LocationchartComponent', () => {
  let component: LocationchartComponent;
  let fixture: ComponentFixture<LocationchartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LocationchartComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LocationchartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
