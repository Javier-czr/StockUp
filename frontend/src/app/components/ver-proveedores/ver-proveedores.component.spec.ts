import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VerProveedoresComponent } from './ver-proveedores.component';

describe('VerProveedoresComponent', () => {
  let component: VerProveedoresComponent;
  let fixture: ComponentFixture<VerProveedoresComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VerProveedoresComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(VerProveedoresComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
