import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IngresarDanadosComponent } from './ingresar-danados.component';

describe('IngresarDanadosComponent', () => {
  let component: IngresarDanadosComponent;
  let fixture: ComponentFixture<IngresarDanadosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [IngresarDanadosComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(IngresarDanadosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
