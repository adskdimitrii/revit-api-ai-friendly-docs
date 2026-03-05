# Bending Detail Custom Field Properties Class

Source: https://www.revitapidocs.com/2026/fca17725-1925-31a4-1a9b-c773c4329e46.htm

---

| Bending Detail Custom Field Properties Class |
| --- |

Represents the properties of a Bending Detail Custom Field. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.Structure BendingDetailCustomFieldProperties 
  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class BendingDetailCustomFieldProperties : ICustomFieldProperties, 
	IDisposable
```

```
Public Class BendingDetailCustomFieldProperties
	Implements ICustomFieldProperties, IDisposable
```

```
public ref class BendingDetailCustomFieldProperties : ICustomFieldProperties, 
	IDisposable
```

```
type BendingDetailCustomFieldProperties = 
    class
        interface ICustomFieldProperties
        interface IDisposable
    end
```
The BendingDetailCustomFieldProperties type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AngularDimensionsDisplayOption](5f7a04d5-121d-48fd-22c1-65cce420802f.htm) | Identifies the angular dimensions display options. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AngularDimensionsEnabled](8420ed02-5b86-dff2-4cc5-7c6307701762.htm) | Identifies if any angular dimensions will be shown or not. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AngularDimensionsForCranksEnabled](Bending-Detail-Custom-Field-Properties-Angular-Dimensions-For-Cranks-Enabled-Property.md) | Identifies if the angular dimensions which has a reference set on a crank will be shown or not. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AngularDimensionsForHooksEnabled](4c49bf38-1e61-a4fe-ebda-fd05e3b90e63.htm) | Identifies if the angular dimensions which has a reference set on a hook will be shown or not. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AngularDimensionsMeasurementOptions](8db4a4ff-0e1b-7615-6bac-f9536beef2b5.htm) | Identifies the measurement option for angular dimensions. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AngularDimensionsOffset](76094859-caa7-30ea-0e1c-cdd4725e2d7e.htm) | Identifies the offset of the angular dimensions. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AngularDimensionTextPosition](40a7f256-c68a-5f3b-9994-885c619b8e03.htm) | Identifies the text position with respect to dimension line. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AngularDimensionTypeId](9831ce4e-0bef-8e07-5260-32d8ecb80a3e.htm) | Identifies the Id of the angular dimension type which is used to show dimensions. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [BendDiameterDimensionsEnabled](5e06f0e4-2980-403f-79d8-a58c70dd5a3e.htm) | Identifies if any radial or diameter dimensions will be shown or not. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [BendDiameterDimensionsForHooksEnabled](6eb8246b-1b2d-5344-babd-4b0eea2c0990.htm) | Identifies if radial or diameter dimensions will be shown for hook fillets  This property has a meaning only if [BendDiameterDimensionsEnabled](5e06f0e4-2980-403f-79d8-a58c70dd5a3e.htm) is set to true. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [BendDiameterDimensionsForSegmentsEnabled](f8d57ff5-95ad-1d65-edb9-73607167f668.htm) | Identifies if radial or diameter dimensions will be shown for the bends between segments.  Radial or diameter dimesions for arc segments will be shown by default.  This property has a menaning only if [BendDiameterDimensionsEnabled](5e06f0e4-2980-403f-79d8-a58c70dd5a3e.htm) is set to true. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [BendDiameterDimensionType](1765eae5-5724-05cf-9308-6aa845a52b1b.htm) | Identifies what type of bend diameter dimensions will be shown (radial or diameter). |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DiameterDimensionTypeId](81f1e17a-7ee5-d3ea-3aaf-6203bb2ff7cb.htm) | Identifies the Id of the diameter dimension type which is used to show dimensions. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](84909688-8680-eef3-d568-36f521510543.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [LineStyleId](c691f2b9-dc2b-d123-8374-4a9e34d67059.htm) | Identifies the line style that is used for drawing Bending Detail curves. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [MultipleValuesIndicatorOption](e1cfec20-7572-6578-ba2a-e9b7a308daae.htm) | Identifies how the Bending Detail will represent the varying rebar dimensions. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [OrthogonalAndOverallDimesionsEnabled](c3e01192-7ad8-4d69-84a1-680d6a66bb74.htm) | Identifies if orthogonal and overall dimensions are displayed. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ParametersDisplayOption](eae872b5-9687-1012-3a5e-5bcf9f3bf977.htm) | Identifies how the parameters will be represented. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [RadialDimensionTypeId](90b4d8ee-1165-0311-579b-99772b0368d7.htm) | Identifies the Id of the radial dimension type which is used to show dimensions. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [RepresentaionOf3DShapes](4149d79c-cbc1-37eb-0c5e-9d201ca569b4.htm) | Identifies how the Bending Detail will represent the 3D shapes. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SegmentLengthDimensionsEnabled](184cbd95-aaaf-e9ab-ecb4-07a065cd51f4.htm) | Identifies if any segment length dimensions will be shown or not. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SegmentLengthDimensionsForHooksEnabled](3a6a3be7-5c2a-7d98-f6c6-2c725b25f4aa.htm) | Identifies if segment length dimensions for hooks will be shown or not.  If this property is true, the [SegmentLengthDimensionsEnabled](184cbd95-aaaf-e9ab-ecb4-07a065cd51f4.htm) should also be true to see segment length dimensions for hooks. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SegmentLengthDimensionsOffset](2c4470fa-1594-ce4f-93a6-8ed868c4bad7.htm) | Identifies the offset of the segment length dimensions. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SegmentLengthDimensionTextPosition](d6917842-00a8-7fbf-8217-0840b38d3a16.htm) | Identifies the text position with respect to dimension line. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SegmentLengthDimensionTypeId](6860f3f3-59b5-74e9-c718-4be700dbe8ac.htm) | Identifies the Id of the linear dimension type which is used to show segments length. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SegmentLengthsDisplayOption](9297e2e5-0c49-73c0-abea-73f008dc52aa.htm) | Identifies if the segment lengths are represented using dimensions or just as text. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SegmentLengthsForArcsDisplayOption](cd040975-377e-9c8a-19a0-190f93d1b5ba.htm) | Identifies if the arc segment lengths are represented using dimensions or just as text.  Only RebarShapes whose definition is RebarShapeDefinitionByArc are considered that have arc segments. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SegmentsRepresentation](53c80d19-4e8a-db59-85df-0abc0f142331.htm) | Identifies how the bending detail will represent the segments of the bar. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AreEqualTo](f18895ca-d558-b438-62f8-fd23f15e14a6.htm) | Identifies if the custom field properties are equal or not. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](d57ea5ef-9825-70d4-fde3-0f29fbcedf32.htm) | Releases all resources used by the BendingDetailCustomFieldProperties |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
