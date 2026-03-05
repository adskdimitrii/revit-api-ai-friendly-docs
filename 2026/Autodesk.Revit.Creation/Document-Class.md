# Document Class

Source: https://www.revitapidocs.com/2026/ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm

---

| Document Class |
| --- |

The Document Creation object is used to create new instances of elements within the
Autodesk Revit project. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
[Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) 
[Autodesk.Revit.Creation ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) 
Autodesk.Revit.Creation Document 
  
**Namespace:** [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class Document : ItemFactoryBase
```

```
Public Class Document
	Inherits ItemFactoryBase
```

```
public ref class Document : public ItemFactoryBase
```

```
type Document = 
    class
        inherit ItemFactoryBase
    end
```
The Document type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsReadOnly](d516bcd2-a3fd-a578-58f6-f1add979bd07.htm) | Identifies if the object is read\-only or modifiable. (Inherited from [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](7c03212a-b587-1c89-3912-efea0d2619c5.htm) | Causes the object to release immediately any resources it may be utilizing. (Inherited from [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewAlignment](b3c10008-aba6-9eee-99c9-7e05ace75796.htm) | Add a new locked alignment into the Autodesk Revit document. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewArea](e7aa9e51-49c2-19b0-9a5b-c1f3ae6a9a1b.htm) | Creates a new area |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewAreaBoundaryConditions(Element, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double)](e75ba4d7-f2e6-e5c1-d695-ef6476a19711.htm) | Creates a new Area BoundaryConditions element on a host element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewAreaBoundaryConditions(Reference, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double)](070c2d73-9a6d-3840-b149-b82bb87d4ed3.htm) | Creates a new Area BoundaryConditions element on a reference. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewAreaBoundaryLine](0a905433-bd87-58d5-903b-344c47ad2519.htm) | Creates a new boundary line as an Area border. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewAreas](2db91e82-ef02-6193-7872-ec64884d437e.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewAreaTag](626eda1c-4259-63f6-22b4-c6c234615a61.htm) | Creates a new area tag. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewCrossFitting](f8175e3f-31d3-7342-054c-4911a239531d.htm) | Add a new family instance of a cross fitting into the Autodesk Revit document, using four connectors. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewCurtainSystem](1599c7f0-c177-4fed-df96-83232424f008.htm) | Creates a new CurtainSystem element from a set of faces. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewCurtainSystem2](e2331d61-7580-3955-56b8-566a9c990fa3.htm) | Creates a new CurtainSystem element from a set of face references. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewDetailCurve](9a8bd0d3-00dc-7a1c-39dd-e891899764ce.htm) | Creates a new detail curve element. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewDetailCurveArray](fa64b91f-d0ff-6793-1fc5-05ca1204a9c5.htm) | Creates an array of new detail curve elements. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewDimension(View, Line, ReferenceArray)](47b3977d-da93-e1a4-8bfa-f23a29e5c4c1.htm) | Creates a new linear dimension object using the default dimension style. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewDimension(View, Line, ReferenceArray, DimensionType)](475aab91-19d3-5884-d3eb-18dfc0d4004f.htm) | Creates a new linear dimension object using the specified dimension style. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewElbowFitting](6f206b7d-f982-bdbd-8342-ed99719e9d81.htm) | Add a new family instance of an elbow fitting into the Autodesk Revit document, using two connectors. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewExtrusionRoof](d165a352-dbd4-a7a5-9734-5423bbfa2543.htm) | Creates a new Extrusion Roof. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFamilyInstance(Face, Line, FamilySymbol)](993bb1aa-d039-d50b-7485-5f404add7cfa.htm) | Inserts a new instance of a family onto a face of an existing element,  using a line on that face for its position, and a type/symbol. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFamilyInstance(Line, FamilySymbol, View)](899076fd-73d2-5be0-8872-b8f389d4ba49.htm) | Add a line based detail family instance into the Autodesk Revit document,  using an line and a view where the instance should be placed. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFamilyInstance(Reference, Line, FamilySymbol)](4545a04f-b5e8-1921-5a4c-d734bc4874ca.htm) | Inserts a new instance of a family onto a face referenced by the input Reference instance,  using a line on that face for its position, and a type/symbol. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFamilyInstance(XYZ, FamilySymbol, StructuralType)](4a037d33-8251-2a50-5470-c98320e2faff.htm) | Inserts a new instance of a family into the document, using a location and a type/symbol. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFamilyInstance(XYZ, FamilySymbol, View)](7499013d-e0d1-df16-92d0-ceefe7cf5c2a.htm) | Add a new family instance into the Autodesk Revit document,  using an origin and a view where the instance should be placed. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFamilyInstance(Curve, FamilySymbol, Level, StructuralType)](d8e0a91a-b062-3a86-6d8e-779534459ff4.htm) | Inserts a new instance of a family into the document,  using a curve, type/symbol and reference level. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFamilyInstance(Face, XYZ, XYZ, FamilySymbol)](3afcdf82-b25c-3092-d42c-b60490075d22.htm) | Inserts a new instance of a family onto a face of an existing element,  using a location, reference direction, and a type/symbol. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFamilyInstance(Reference, XYZ, XYZ, FamilySymbol)](be4b822c-829a-7e7b-8c03-a3a324bfb75b.htm) | Inserts a new instance of a family onto a face referenced by the input Reference instance,  using a location, reference direction, and a type/symbol. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFamilyInstance(XYZ, FamilySymbol, Element, StructuralType)](61601fe7-6d7e-e600-192d-207aa31c381c.htm) | Inserts a new instance of a family into the document, using a location, type/symbol, and the host element. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFamilyInstance(XYZ, FamilySymbol, Level, StructuralType)](5cc3f69b-7782-8e4c-2b4e-4fe4495217ae.htm) | Inserts a new instance of a family into the document, using a location, type/symbol, and the level. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFamilyInstance(XYZ, FamilySymbol, Element, Level, StructuralType)](168d4c67-73dd-d7c8-4969-12846eeaddfa.htm) | Inserts a new instance of a family into the document, using a location, type/symbol, the host element and a base level. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFamilyInstance(XYZ, FamilySymbol, XYZ, Element, StructuralType)](7febcfdb-dbfa-317a-1c5e-882621f3e846.htm) | Inserts a new instance of a family into the document, using a location, type/symbol, the host element and a reference direction. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFamilyInstances2](6ce99315-7b3d-6e29-73da-eb701b9dd064.htm) | (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFascia(FasciaType, Reference)](b718bf71-309b-f512-fc21-e08012cec091.htm) | Creates a fascia along a reference. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFascia(FasciaType, ReferenceArray)](1805a23b-4de5-2f8d-0ceb-4f61256fdf23.htm) | Creates a fascia along a reference array. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFlexDuct(IList XYZ , FlexDuctType)](860d0483-974f-c270-454b-625ab8f85b31.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFlexDuct(Connector, Connector, FlexDuctType)](0910f241-d976-2ee8-496d-268a44725d13.htm) | Adds a new flexible duct into the document,  using two connector, and duct type. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFlexDuct(Connector, IList XYZ , FlexDuctType)](3f73b205-4121-eb63-c6de-d31fd1c74be7.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFlexPipe(IList XYZ , FlexPipeType)](4c34f62d-8690-fcf4-5606-9cf42b703f2e.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFlexPipe(Connector, Connector, FlexPipeType)](d43da744-8bf9-b2a5-e489-67e6d46bef2a.htm) | Adds a new flexible pipe into the document,  using two connector, and flexible pipe type. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFlexPipe(Connector, IList XYZ , FlexPipeType)](1a0bb277-6f31-b344-bbcc-e5593826ae54.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewFootPrintRoof](110741bf-b041-9f78-0832-ec9f5892cebc.htm) | Creates a new FootPrintRoof element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewGroup](8bdb7337-7063-cff8-28a4-958464f2fa5b.htm) | (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewGutter(GutterType, Reference)](5213092c-0c83-5ba5-4f3a-871a1a93f368.htm) | Creates a gutter along a reference. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewGutter(GutterType, ReferenceArray)](46c49562-965d-6819-d2c4-05d1211fc960.htm) | Creates a gutter along a reference array. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewLineBoundaryConditions(Element, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double)](763b3890-cac4-32c6-69c6-e4ebe6cfdd6e.htm) | Creates a new Line BoundaryConditions element on a host element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewLineBoundaryConditions(Reference, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double)](f2b3d99a-9760-89df-9531-6434ad30de92.htm) | Creates a new Line BoundaryConditions element on a reference. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewMechanicalSystem](d9d6fd18-6cf3-d7d3-31a1-d7d7ef45cfa0.htm) | Creates a new MEP mechanical system element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewModelCurve](b880c4d7-9841-e44e-2a1c-36fefe274e2e.htm) | Creates a new model line element. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewModelCurveArray](12beb77b-e5fe-1499-7da3-78742dba3303.htm) | Creates an array of new model line elements. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewOpening(Element, CurveArray, eRefFace)](73c9751f-df8c-04cc-e628-81e582f5c777.htm) | Creates a new opening in a beam, brace and column. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewOpening(Element, CurveArray, Boolean)](8ff3c649-4d5a-67a6-81d7-3d1dca9e9955.htm) | Creates a new opening in a roof, floor and ceiling. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewOpening(Level, Level, CurveArray)](871161b1-a154-be20-f256-6f9141100905.htm) | Creates a new shaft opening between a set of levels. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewOpening(Wall, XYZ, XYZ)](06a216d4-2cf6-ec8f-df5b-10f007b70531.htm) | Creates a rectangular opening on a wall. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewPipingSystem](ce8ca4d6-8fb3-fe68-c5e3-6970c00a9a2b.htm) | Creates a new MEP piping system element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewPointBoundaryConditions](db4e68f0-d06c-8207-98fb-83e84b3cb2d1.htm) | Creates a new Point BoundaryConditions Element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewReferencePlane](1c618038-3801-0f60-9c12-a5923dc87a2c.htm) | Creates a new instance of ReferencePlane. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewReferencePlane2](8db0c9ac-9dd9-72b8-3939-c1a1c605fb49.htm) | Creates a new instance of ReferencePlane. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewRoom(Phase)](0bf2d8e2-593f-1ba7-c0dc-5274749abe19.htm) | Creates a new unplaced room and with an assigned phase. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewRoom(Level, UV)](28262c8c-d18a-338c-eb17-f406438949d8.htm) | Creates a new room on a level at a specified point. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewRoom(Room, PlanCircuit)](9ceb1869-e41b-8a3f-557c-0b13eb062e0b.htm) | Creates a new room within the confines of a plan circuit, or places an unplaced room within the confines of the plan circuit. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewRoomBoundaryLines](cd40f8d3-e6cf-355e-d3c4-b3296e261485.htm) | Creates a new boundary line as an Room border. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewRooms2(Level)](5d5f7f56-c86c-d87e-ff6c-eb4e465a5183.htm) | Creates new rooms in each plan circuit found in the given level in the last phase. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewRooms2(Level, Phase)](716dba64-4853-685b-bb3f-6c071b0cd0c8.htm) | Creates new rooms in each plan circuit found in the given level in the given phase. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewRooms2(Phase, Int32\)](d17f1295-77c6-f8ca-2e5e-6351ef0f520a.htm) | Creates new unplaced rooms in the given phase. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewRoomTag](9847aafe-42f9-fe8e-5229-c491add7ec46.htm) | Creates a new RoomTag referencing a room in the host model or in a Revit link. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewSlabEdge(SlabEdgeType, Reference)](dbd42278-f7b8-03e3-b8b9-add9eb65022f.htm) | Creates a slab edge along a reference. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewSlabEdge(SlabEdgeType, ReferenceArray)](fb368db2-914d-5867-0c4b-2380fbd3db49.htm) | Creates a slab edge along a reference array. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewSpace(Phase)](ea6a14cd-5ffb-4220-e4d4-401a44c8234b.htm) | Creates a new unplaced space on a given phase. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewSpace(Level, UV)](43059324-6e95-706b-ea39-627601d0419c.htm) | Creates a new space element on the given level at the given location. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewSpace(Level, Phase, UV)](ce49bd88-7d6b-b3ca-bd4c-497233718ffb.htm) | Creates a new space element on the given level, at the given location, and assigned to the given phase. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewSpaceBoundaryLines](e95433bf-3440-50e3-c9d0-c5559fbb0aff.htm) | Creates a new boundary line as an Space border. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewSpaces2(Phase, Int32\)](5727a24c-310b-a76f-b9fa-0a7b0697e902.htm) | Creates a set of new unplaced spaces on a given phase. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewSpaces2(Level, Phase, View)](94b4e479-2301-2e78-6201-5bb5614ed796.htm) | Creates new spaces on the available plan circuits of a the given level. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewSpaceTag](07f23ff4-61c1-54a4-8332-0c9dbcdad556.htm) | Creates a new SpaceTag. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewSpotCoordinate](c2efc79c-75ff-4505-ef3d-3db94a952227.htm) | Generate a new spot coordinate object within the project. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewSpotElevation](b9cea807-b0f5-9e59-463d-c633221d1590.htm) | Generate a new spot elevation object within the project. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewTakeoffFitting](9aef4be8-349b-ee4c-c1bc-b41d6211c79c.htm) | Add a new family instance of an takeoff fitting into the Autodesk Revit document, using one connector and one MEP curve. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewTeeFitting](c261a205-f1fc-8552-6e8f-8c81186b6b6d.htm) | Add a new family instance of a tee fitting into the Autodesk Revit document, using three connectors. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewTransitionFitting](1dcbaa41-5881-b807-b333-10855acb408e.htm) | Add a new family instance of an transition fitting into the Autodesk Revit document, using two connectors. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewUnionFitting](Document-New-Union-Fitting-Method.md) | Add a new family instance of an union fitting into the Autodesk Revit document, using two connectors. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NewZone](Document-New-Zone-Method.md) | **Obsolete.** Creates a new Zone element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [PlaceGroup](586d4f2e-0985-2d0b-dbb7-ea6d2f704336.htm) | Place an instance of a Model Group into the Autodesk Revit document, using a location and a group type. (Inherited from [ItemFactoryBase](cba2c84a-22c0-e6e7-a99c-67656901853a.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The Document Creation object is a utility object that is used to create new
instances of elements within the Autodesk Revit project. This object, available from the
Document.Create property should be used to create elements instead of using New. This
object ensures that the elements created are added to the document correctly. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)
