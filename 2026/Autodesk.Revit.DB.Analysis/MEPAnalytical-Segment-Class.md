# MEPAnalytical Segment Class

Source: https://www.revitapidocs.com/2026/64b45968-97cf-a797-09a6-4583ad9069f7.htm

---

| MEPAnalytical Segment Class |
| --- |

Represents an analytical segment of the MEP analytical model. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.Analysis MEPAnalyticalSegment 
  
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class MEPAnalyticalSegment : IDisposable
```

```
Public Class MEPAnalyticalSegment
	Implements IDisposable
```

```
public ref class MEPAnalyticalSegment : IDisposable
```

```
type MEPAnalyticalSegment = 
    class
        interface IDisposable
    end
```
The MEPAnalyticalSegment type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Area](392f2129-7be9-c59a-762d-3e438e323c7e.htm) | The area of the segment profile. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DemandFlow](eaba9409-603d-7e3e-71cc-436415d408a5.htm) | The designed flow value, in ft^3/s. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DomainType](e7c71782-0730-876f-95d1-e928e6e74880.htm) | The connector domain type of this segment. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [EndNode](8650c34e-7842-892f-f31a-449112b6d57d.htm) | The id of the end analytical node. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Id](ca7e1bcf-41a5-d256-7741-850a14b9c08f.htm) | The identity of this segment. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [InnerDiameter](f0553bf0-81ee-1cec-f216-4f8beddb1dbf.htm) | The inner diameter of this segment, in ft. For rectangular or oval profile, this may be the hydraulic diameter. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](a037f686-806c-7f76-7fc0-872cdb3b607b.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [OverrideType](MEPAnalytical-Segment-Override-Type-Property.md) | The override type of analytical segment pressure loss calculation. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [RevitElementId](ea394f2e-6929-ca71-5ebd-6c29566a39bf.htm) | The id of the owning Revit element. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Roughness](5b089154-9759-741e-e5ed-877a093e8c74.htm) | The roughness of this segment, in ft. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SegmentType](22cc893f-ad98-ea95-a30c-3bf108364dcb.htm) | The analytical segment type. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [StartNode](8ea58f28-f362-9c3b-b623-3e84e4e48242.htm) | The id of the start analytical node. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](1ac1a866-279d-41c2-696f-8a53e1a08645.htm) | Releases all resources used by the MEPAnalyticalSegment |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetFlowCharacteristics](MEPAnalytical-Segment-Get-Flow-Characteristics-Method.md) | Gets all flow characteristics of the segment. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetFlowConvergenceCharacteristic](MEPAnalytical-Segment-Get-Flow-Convergence-Characteristic-Method.md) | Gets the flow convergence characteristic of the segment. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetFlowTransitionCharacteristic](MEPAnalytical-Segment-Get-Flow-Transition-Characteristic-Method.md) | Gets the flow transition characteristic of the segment. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetLossCoefficientOverride](MEPAnalytical-Segment-Get-Loss-Coefficient-Override-Method.md) | Gets the overridden value of loss coefficient, dimensionless. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetNetworkSegmentId](f9baea4a-46d9-52e8-982e-a56dbf151faf.htm) | Gets the NetworkSegmentId. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetPressureDropOverride](MEPAnalytical-Segment-Get-Pressure-Drop-Override-Method.md) | Gets the overidden value of pressuer drop, in kg/(ft\*s^2\). |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsSegmentOverridable](MEPAnalytical-Segment-Is-Segment-Overridable-Method.md) | Verifies if the segment can be overridden (e.g., the pressure drop of the pump and curve segments are calculated from the network and cannot be overridden). |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetLossCoefficientOverride](MEPAnalytical-Segment-Set-Loss-Coefficient-Override-Method.md) | Sets the overridden value of loss coefficient. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetOverrideType](MEPAnalytical-Segment-Set-Override-Type-Method.md) | Sets the override type of pressure loss calculation. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetPressureDropOverride](MEPAnalytical-Segment-Set-Pressure-Drop-Override-Method.md) | Sets the overridden value of pressure drop. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
