"""Output schema for bpl-cards.

Keep each Field(description=...) short and structural — behaviour and edge cases
belong in prompt.md, which is also sent to the model.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Record(BaseModel):
    call_number: Optional[str] = Field(None, description="Shelfmark, e.g. 'PN2589 .C4'")
    heading: Optional[str] = Field(None, description="Subject/added heading as printed")
    author: Optional[str] = Field(None, description="Main entry, surname first")
    title: Optional[str] = Field(None, description="Title of the work")
    imprint: Optional[str] = Field(None, description="Place, publisher, date")
    collation: Optional[str] = Field(None, description="Pagination, illustrations, size")
    notes: Optional[str] = Field(None, description="Contents or other card notes")
